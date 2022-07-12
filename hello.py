import pandas as pd
import numpy as np
import speech_recognition as sr
from io import StringIO

print("inicio----------------------------------------------------------------------------------")
filename = "pc_diga5min"

r = sr.Recognizer()

AUDIO_FILE = f"{filename}.wav"

with sr.AudioFile(AUDIO_FILE) as source:

        audio = r.record(source)  # read the entire audio file                  

        text = r.recognize_google(audio, language="pt-pt")
        print(text)

#***************************************************************PANDAS ***********************
df = pd.DataFrame({'mytext': [text]}) #creat data frame 
new_df = df.mytext.str.split(expand=True).stack().value_counts().reset_index() #count words frequency 
new_df.columns = ['Word', 'Frequency'] 
 
#print(new_df.columns)
#**************************************************************************************
#**********************search words******************************************************************


import yake
kw_extractor = yake.KeywordExtractor(top=10, stopwords=None)
keywords = kw_extractor.extract_keywords(text)
#for kw, v in keywords:
 # print("Keyphrase: ",kw, ": score", v)
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------

import spacy
import pytextrank

nlp = spacy.load("en_core_web_sm")
# add PyTextRank to the spaCy pipeline
nlp.add_pipe("textrank")

doc = nlp(text)
# examine the top-ranked phrases in the document
#print("spacy----------------------------------------------------------------------------------")
for phrase in doc._.phrases:
 #   print(phrase.text)
    if(phrase.rank >0.01):
        print(phrase.text,phrase.rank, phrase.count)
   # print(phrase.chunks)
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------

from keybert import KeyBERT
kw_model = KeyBERT()
keywords = kw_model.extract_keywords(text)

print(kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words=None)) 
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
