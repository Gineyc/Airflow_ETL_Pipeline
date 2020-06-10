import re
import os
import pandas as pd
from textblob import TextBlob

if __name__ == "__main__":
    DAG_FOLDER = os.path.abspath(os.path.dirname(__file__))
    OUTPUT_FOLDER = os.path.join(DAG_FOLDER,"..", "output")

    file1 = OUTPUT_FOLDER+'/clean_text.csv'
    df=pd.read_csv(file1,index_col=None,encoding='utf-8')
    textblob_SA=[]
    textblob_poly=[]
    for i in df["cleaned_text"]:
        analsysis=TextBlob(i)
        textblob_SA.append(analsysis.sentiment.polarity)
        if analsysis.sentiment.polarity>=0.1:
            textblob_poly.append("Positive")
        elif analsysis.sentiment.polarity<=-0.1:
            textblob_poly.append("Negative")
        else:
            textblob_poly.append("Neutral")
    df["textblob_SA"]=textblob_SA
    df["textblob_poly"]=textblob_poly
    name=OUTPUT_FOLDER+'/add_textblob.csv'
    df.to_csv(name,header=True,index=False,encoding='utf_8_sig')
