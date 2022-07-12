import speech_recognition as sr
import numpy as np
import os
import sys

file = "pcdiga_completo.wav"

print("Entrou Transcript com filname: " + file)

r = sr.Recognizer()

filename, ext = os.path.splitext(file)

AUDIO_FILE = f"{filename}.wav"

with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

# does transcription of audio
text = r.recognize_google(audio, language="pt-PT")

print(text)

with open(f"{filename}.txt", 'w') as f:
    f.write(text)

