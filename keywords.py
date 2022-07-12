import speech_recognition as sr
import pandas as pd

def keywords(text):

    df = pd.DataFrame({'mytext': [text]})
    
    df["mytext_new"] = df['mytext'].str.lower().str.replace('[^\w\s]','')

    new_df = df.mytext_new.str.split(expand=True).stack().value_counts().reset_index()
    
    new_df.columns = ['Word', 'Frequency'] 

    return new_df.astype(str)