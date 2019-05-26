from gtts import gTTS
from playsound import playsound
from tempfile import mktemp, TemporaryFile
from os import remove

def text_to_speech(text):
    tts = gTTS(text, lang='en')
    filename = mktemp(prefix='tts_temp_audio', suffix='.mp3', dir='')
    with open(filename, 'wb') as f:
        tts.write_to_fp(f)
    # filename = TemporaryFile()
    # tts.save(filename)
    playsound(filename)
    # filename.close()
    remove(filename)