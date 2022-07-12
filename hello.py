import pandas as pd
import numpy as np
import speech_recognition as sr
from io import StringIO
 
filename = "clip-pt"

r = sr.Recognizer()

AUDIO_FILE = f"{filename}.wav"

with sr.AudioFile(AUDIO_FILE) as source:

        audio = r.record(source)  # read the entire audio file                  

        text = r.recognize_google(audio, language="pt-PT")
        print(text)


#StringData = StringIO(text)
 
df = pd.DataFrame({'mytext': [text]})
 
df["mytext_new"] = df['mytext'].str.lower().str.replace('[^\w\s]','')
new_df = df.mytext_new.str.split(expand=True).stack().value_counts().reset_index()
 
new_df.columns = ['Word', 'Frequency'] 
 
print(new_df)


