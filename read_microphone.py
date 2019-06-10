import queue
import sys
import tempfile
import time as timetime
from statistics import mean
from collections import deque
import os

def record_audio_no_duration():
    try:
        import sounddevice as sd
        import soundfile as sf
        import numpy  # Make sure NumPy is loaded before it is used in the callback
        assert numpy  # avoid "imported but unused" message (W0611)

        # input('Press enter to start recording')
        filename = tempfile.mktemp(prefix='alexa_temp_audio_', suffix='.wav', dir='')

        device_info = sd.query_devices(None, 'input')
        # soundfile expects an int, sounddevice provides a float:
        samplerate = int(device_info['default_samplerate'])

        channels = 1
        q = queue.Queue()
        start = timetime.time()
        global flag
        flag = True
        vol = {}
        last_two_seconds = deque()
        global started
        started = False

        def callback(indata, frames, time, status):
            global started
            global flag
            threshold = 5
            """This is called (from a separate thread) for each audio block."""
            if status:
                print(status, file=sys.stderr)
            volume_norm = int(numpy.linalg.norm(indata) * 10)
            if len(last_two_seconds) > 39*2:
                last_two_seconds.popleft()
            last_two_seconds.append(volume_norm)
            avg = mean(last_two_seconds)
            if len(last_two_seconds) > 39*2:
                # and avg > threshold:
                started = True

            if started and avg < threshold:
                flag = False
            # cr_time = timetime.time()
            # # delta = int(cr_time - start)
            # # if delta not in vol:
            # #     vol[delta] = []
            # #     if delta != 0:
            # #         print(delta, mean(vol[delta - 1]), len(vol[delta - 1]))
            # # vol[delta].append(volume_norm)
            # global flag
            # if int(cr_time - start) > 5:
            #     flag = False

            # print("|" * int(volume_norm))
            q.put(indata.copy())

        # Make sure the file is opened before recording anything:
        with sf.SoundFile(filename, mode='x', samplerate=samplerate,
                          channels=channels, subtype='PCM_16') as file:
            with sd.InputStream(samplerate=samplerate,
                                channels=channels, callback=callback):
                # print('#' * 80)
                # print('press Ctrl+C to stop the recording')
                # print('#' * 80)
                while flag:
                    file.write(q.get())

    except KeyboardInterrupt:
        print('\nRecording finished: ' + repr(filename))
    from google_api import transcribe
    cmd = transcribe(filename)
    os.remove(filename)
    return cmd.lower()
    # print(cmd)

    # return filename


if __name__ == '__main__':
    record_audio_no_duration()