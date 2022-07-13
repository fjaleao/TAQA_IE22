import os
import sys
from transcript import transcript

def merge_txt_splitVideo(numberSplits,file):

    filename = os.path.splitext(file)
    
    with open(f"{filename}.txt", 'w') as f:
        for number in range(0,numberSplits,1):
            #f.write(transcript((str(number) + '_' + file), "pt-PT", 1))
            print(transcript((str(number) + '_' + file), "pt-PT", 1))
   
    f.close()
       
merge_txt_splitVideo(7,"pcdiga_completo")