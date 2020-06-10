import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os
import pandas as pd

if __name__ == "__main__":
    nltk_vsa=[]
    nltk_poly=[]
    sid=SentimentIntensityAnalyzer()
    DAG_FOLDER = os.path.abspath(os.path.dirname(__file__))
    OUTPUT_FOLDER = os.path.join(DAG_FOLDER,"..", "output")

    file1 = OUTPUT_FOLDER+'/clean_text.csv'
    df=pd.read_csv(file1,index_col=None,encoding='utf-8')

    for i in df["cleaned_text"]:
        nltk_vsa.append(sid.polarity_scores(i)['compound'])
        if sid.polarity_scores(i)['compound']>=0.1:
            nltk_poly.append("Positive")
        elif sid.polarity_scores(i)['compound']<=-0.1:
            nltk_poly.append("Negative")
        else:
            nltk_poly.append("Neutral")
            
    df["nltk_vsa"]=nltk_vsa
    df["nltk_poly"]=nltk_poly
    name=OUTPUT_FOLDER+'/add_nltk.csv'
    df.to_csv(name,header=True,index=False,encoding='utf_8_sig')
