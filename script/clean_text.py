import re
import os
import pandas as pd
DAG_FOLDER = os.path.abspath(os.path.dirname(__file__))
OUTPUT_FOLDER = os.path.join(DAG_FOLDER,"..", "output")

def data_clean(text):
    p=re.compile(r'[-,$()#+&*]')
    urlclean=re.compile(r'https://[a-zA-Z0-9.?/&=:]*',re.S)
    tagclean=re.compile(r'#[a-zA-Z0-9.?/&=:_]*',re.S)
    userclean=re.compile(r'@[a-zA-Z0-9.?/&=:_]*',re.S)
    cleaned_text=[]

    for i in text:
        nourl=re.sub(urlclean,"",i)
        nouser=re.sub(userclean,"",nourl)
        notag=re.sub(tagclean,"",nouser)
        clean =notag.replace('\n',"")
        cleaned_text.append(clean)
    return cleaned_text


if __name__ == "__main__":
    # read csv filr from clean_test.csv
    file1 = OUTPUT_FOLDER+'/clean_hashtag.csv'
    df=pd.read_csv(file1,index_col=None,encoding='utf-8')
    # call function
    df['cleaned_text'] = data_clean(df['original_text'])
    # save to output folder
    name=OUTPUT_FOLDER+'/clean_text.csv'
    df.to_csv(name,header=True,index=False,encoding='utf_8_sig')

