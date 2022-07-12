import pandas as pd
import numpy as np
 
 
df = pd.DataFrame({'mytext':['I love Predictive Hacks!','How can I remove punctuations?'
                             ,'He said: "This is cool!".']})
 


 
df["mytext_new"] = df['mytext'].str.lower().str.replace('[^\w\s]','')
new_df = df.mytext_new.str.split(expand=True).stack().value_counts().reset_index()
 
new_df.columns = ['Word', 'Frequency'] 
 
print(new_df)


