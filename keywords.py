from pickle import FALSE
import speech_recognition as sr
import pandas as pd
import numpy as np
import spacy
import pytextrank
from keybert import KeyBERT
from sentence_transformers import SentenceTransformer
from IPython.display import display

def keywords(text):
  
    #words frequency

    df = pd.DataFrame({'mytext': [text]})
  #  df["mytext_new"] = df['mytext'].str.lower().str.replace('[^\w\s]','') #replace special caracters
    
    new_df = df.mytext.str.split(expand=True).stack().value_counts().reset_index()  # count wodrs frequency
    new_df.columns = ['Word', 'Frequency']      
        
    pd.set_option('display.max_rows',None)    #show all results
    print(new_df.astype(str))                 # print words frequency

    with open('readme.txt', 'w') as f:
        f.write(str(new_df.astype(str)))    #print to txt results

    return new_df.astype(str)               #return results ( words frequency )

def keyword_spacy(text):
    #extract keywords spacy - textrank

    nlp = spacy.load("en_core_web_sm")
    # add PyTextRank to the spaCy pipeline
    nlp.add_pipe("textrank")

    doc = nlp(text)
    # examine the top-ranked phrases in the document
    print("spacy----------------------------------------------------------------------------------")

    text_total =" "

    for phrase in doc._.phrases:
    #   print(phrase.text)
        if(phrase.rank >0.01):  #exclude no important results
            text_total += phrase.text + " " + (str)(phrase.rank) + " "+ (str)(phrase.count) + " " # agregate results           
   
    print(text_total) 
    return text_total 


def keyword_keyBert(text):

    #extract keywords keyBert--------------------------------------------------------------------
    print("KeyBert----------------------------------------------------------------------------------")

   # kw_model = KeyBERT()
   
   # sentence_model = SentenceTransformer("distiluse-base-multilingual-cased-v1") #multi language sentence model 
   # sentence_model = SentenceTransformer("all-MiniLM-L6-v2") # English sentence model  
    sentence_model = SentenceTransformer("paraphrase-mpnet-base-v2") #english best, but slower
   
    kw_model = KeyBERT(model=sentence_model)
   # keywords = kw_model.extract_keywords(text) #extract key words no filter
   
   # text = kw_model.extract_keywords(text,keyphrase_ngram_range=(1, 3), stop_words=None, #  Maximal Marginal Relevance
   #                          use_mmr=True, diversity=0.7, top_n=10)                              
    
    text = kw_model.extract_keywords(text, keyphrase_ngram_range=(3, 3), stop_words=None, # Max Sum Similarity
                              use_maxsum=True, nr_candidates=20, top_n=10)
    print(text)
    return (text)