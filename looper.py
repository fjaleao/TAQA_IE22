import os
import sys
from transcript import transcript
from keywords import keyword_keyBert
from keywords import keyword_spacy

def merge_txt_splitVideo(numberSplits,file, lang):

   # filename =  os.getcwd() + "\\IO"  
    filename, ext = os.path.splitext(file)
    
    text_total = " "

    for number in range(0, numberSplits+1 ,1):
     text_total += transcript(("IO/"+str(number) + '_' + file), lang, 1)

    with open(f"{filename}.txt", 'w') as f:
         f.write(text_total)
    
    f.close()
    return(text_total)

#text = merge_txt_splitVideo(2,"eng") #number of cuts 0,1,2 = 2
#keyword_spacy(text)
#keyword_keyBert(text)