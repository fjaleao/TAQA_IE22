import os
import sys
from transcript import transcript
from keywords import* 
from wordCloud import wordCloudGenerate

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
#cut videos 1txt total

#text = merge_txt_splitVideo(54,"teste_entervista_user1.wav") #number of cuts 0,1,2 = 2
#text = merge_txt_splitVideo(2,"eng.wav") #number of cuts 0,1,2 = 2  
#text = merge_txt_splitVideo(13,"transcript_javaScrip.wav") #number of cuts 0,1,2 = 2  

#read txt from file
text =" "
with open('transcript_javaScrip.txt') as f:
    text = str(f.readlines())

result=keyword_spacy(text)    #a lot results
result1=str(keyword_keyBert(text)) # few results
#keywords(text)

#with open('transcript_javaScrip_result.txt', 'w') as f:
 #        f.write(result)

wordCloudGenerate(result1,1) #smal image
wordCloudGenerate(result,0) 

from PIL import Image
 
# Read image
img = Image.open('imagecoreTopic.jpeg')
 
# Output Images
img.show()
#----------------------------------teste palvras por -----------------------
#for number in range(0, 54+1 ,1):
 #   with open("IO/"+str(number) + '_' + "teste_entervista_user1.txt")as f:
  #      text = str(f.readlines())
        #keyword_keyBert(text) 
        #keyword_spacy(text)
        #keywords(text)
        #print("\n")