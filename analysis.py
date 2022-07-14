from defer import return_value
import pandas as pd
import numpy as np
import speech_recognition as sr
from io import StringIO


def analysis(text):
    import spacy
    import pytextrank

    nlp = spacy.load("en_core_web_sm")
    # add PyTextRank to the spaCy pipeline
    nlp.add_pipe("textrank")

    print(text)
    doc = nlp(text)
    # examine the top-ranked phrases in the document
    print("spacy----------------------------------------------------------------------------------")
    list_aux=[]
    for phrase in doc._.phrases:
        #   print(phrase.text)
        if(phrase.rank > 0.01):
            list_aux.append("Text: " + str(phrase.text) + "\t Rank: "+ str(phrase.rank) + "\t Count: " + str(phrase.count))
            print(phrase.text, phrase.rank, phrase.count)
    # print(phrase.chunks)
    # ---------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------

    from keybert import KeyBERT
    kw_model = KeyBERT()
    keywords = kw_model.extract_keywords(text)

    return list_aux
