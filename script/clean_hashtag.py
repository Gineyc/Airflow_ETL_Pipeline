import re
import os
import pandas as pd
DAG_FOLDER = os.path.abspath(os.path.dirname(__file__))
OUTPUT_FOLDER = os.path.join(DAG_FOLDER,"..", "output")
    
def extract_hashtag(text):
    hashtag=[]
    for i in text:
        a=re.findall(r"#(\w+)", i)
        hashtag.append([i.capitalize() for i in a])
    return hashtag

if __name__ == "__main__":
    # merge two temp file into a dataframe
    file1 = OUTPUT_FOLDER+'/temp_vegan.csv'
    file2 = OUTPUT_FOLDER+'/temp_plantbased.csv'
    df=pd.read_csv(file1,index_col=None,encoding='utf-8')
    df1=pd.read_csv(file2,index_col=None,encoding='utf-8')
    df=df.append(df1)
    # call function
    df['hashtag'] = extract_hashtag(df['original_text'])
    # save to output folder
    name=OUTPUT_FOLDER+'/clean_hashtag.csv'
    df.to_csv(name,header=True,index=False,encoding='utf_8_sig')
