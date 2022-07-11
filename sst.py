#IMPORTS
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
import numpy as np

filename = "JIcut"

from pydub import AudioSegment

r = sr.Recognizer()

AUDIO_FILE = f"{filename}.wav"

with sr.AudioFile(AUDIO_FILE) as source:

        audio = r.record(source)  # read the entire audio file                  

        text = r.recognize_sphinx(audio, language="en-US")

with open(f"{filename}.txt", 'w') as f:
    f.write(text)

