import google_api
import read_microphone
import os
import tempfile

if __name__ == '__main__':
    while True:
        input('Press enter to start recording')
        filename = tempfile.mktemp(prefix='alexa_temp_audio', suffix='.wav', dir='')
        read_microphone.record_audio_no_duration(filename)
        recognized = google_api.transcribe(filename)
        os.remove(filename)