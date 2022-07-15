# Python program to generate WordCloud
 
# importing all necessary modules
import os
import sys
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

def wordCloudGenerate(input, small):  
    # Reads '-.txt' file
    #with open(filename) as f:
    text_read = input #str(f.readlines())
    text = text_read.replace("'", "")
    
    if(small):
        wordcloud = WordCloud(width = 500, height = 300,
                        background_color ='gainsboro', colormap = "Reds", random_state=0, max_font_size=50, min_font_size =15,
                        max_words = 500 ).generate(text)
        wordcloud.to_file("imagecoreTopic.pdf")
        wordcloud.to_file("imagecoreTopic.jpeg")

    elif(small == 0):
        wordcloud = WordCloud(width = 800, height = 800,
                        background_color ='gainsboro', colormap = "Reds", random_state=0, max_font_size=50, min_font_size =15,
                        max_words = 500 ).generate(text)  
        wordcloud.to_file("imageHigthdiversity.pdf")
        wordcloud.to_file("imageHigthdiversity.jpeg")               

    return wordcloud
    # plot the WordCloud image                      
    #plt.figure(figsize = (6, 6), facecolor = None)
    #plt.imshow(wordcloud)
    #plt.axis("off")
    #plt.tight_layout(pad = 0)
    
    #plt.show()
    
#teste
#wordCloudGenerate('transcript_javaScrip_result.txt')