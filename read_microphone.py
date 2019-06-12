from queue import Queue
import sys
from tempfile import mktemp
from statistics import mean
from collections import deque
import sounddevice as sd
import soundfile as sf
import numpy
import pickle

def record_audio_no_duration():
    try:
        filename = mktemp(prefix='alexa_temp_audio_', suffix='.wav', dir='')

        device_info = sd.query_devices(None, 'input')
        # soundfile expects an int, sounddevice provides a float:
        samplerate = int(device_info['default_samplerate'])

        #load settings
        with open('saved_settings.settings', 'rb') as infile:
            settings = pickle.load(infile)


        channels = 1
        q = Queue()
        global flag
        flag = True
        last_two_seconds = deque()
        global started
        started = False
        global threshold
        threshold = settings.get_min_volume()/2

        def callback(indata, frames, time, status):
            """This is called (from a separate thread) for each audio block."""
            global started
            global flag
            global threshold
            if status:
                print(status, file=sys.stderr)
            volume_norm = int(numpy.linalg.norm(indata) * 10)
            if len(last_two_seconds) > 39*2:
                last_two_seconds.popleft()
            last_two_seconds.append(volume_norm)
            avg = mean(last_two_seconds)
            if len(last_two_seconds) > 39*2:
                started = True

            if started and avg < threshold:
                flag = False

            q.put(indata.copy())

        # Make sure the file is opened before recording anything:
        with sf.SoundFile(filename, mode='x', samplerate=samplerate,
                          channels=channels, subtype='PCM_16') as file:
            with sd.InputStream(samplerate=samplerate,
                                channels=channels, callback=callback):
                while flag:
                    file.write(q.get())

    except KeyboardInterrupt:
        print('\nRecording finished: ' + repr(filename))
    return filename


if __name__ == '__main__':
    record_audio_no_duration()