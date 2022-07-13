import pandas as pd
import numpy as np
import speech_recognition as sr
from io import StringIO

def analysis(text):
    import yake
    kw_extractor = yake.KeywordExtractor(top=10, stopwords=None)
    keywords = kw_extractor.extract_keywords(text)
