#IMPORTS
import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

AUDIO_FILE = "examples_english.wav"
                                 
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file                  

        print("Transcription: " + r.recognize_google(audio))
