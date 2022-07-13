import speech_recognition as sr
import pandas as pd
import numpy as np
import spacy
import pytextrank
from keybert import KeyBERT

def keywords(text):

    df = pd.DataFrame({'mytext': [text]})
    
    df["mytext_new"] = df['mytext'].str.lower().str.replace('[^\w\s]','')

    new_df = df.mytext_new.str.split(expand=True).stack().value_counts().reset_index()
    
    new_df.columns = ['Word', 'Frequency'] 

    return new_df.astype(str)

def keyword_spacy(text):

    nlp = spacy.load("en_core_web_sm")
    # add PyTextRank to the spaCy pipeline
    nlp.add_pipe("textrank")

    doc = nlp(text)
    # examine the top-ranked phrases in the document
    print("spacy----------------------------------------------------------------------------------")

    text_total =" "

    for phrase in doc._.phrases:
    #   print(phrase.text)
        if(phrase.rank >0.01):
            text_total += phrase.text + " " + (str)(phrase.rank) + " "+ (str)(phrase.count) + " "            
    #---------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------
    print(text_total)
    return text_total


def keyword_keyBert(text):
    print("KeyBert----------------------------------------------------------------------------------")

    kw_model = KeyBERT()
    keywords = kw_model.extract_keywords(text)
   
    text = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words=None)
    print(text) 
    return (text)
    #---------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------