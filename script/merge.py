import pandas as pd
import os

DAG_FOLDER = os.path.abspath(os.path.dirname(__file__))
OUTPUT_FOLDER = os.path.join(DAG_FOLDER,"..", "output")

file1 = OUTPUT_FOLDER+'/add_textblob.csv'
file2 = OUTPUT_FOLDER+'/add_nltk.csv'
df1=pd.read_csv(file1,index_col=None,encoding='utf-8')
df2=pd.read_csv(file2,index_col=None,encoding='utf-8')

on=[i for i in list(df1.columns) if i in list(df2.columns)]
df=df1.merge(df2,how='outer',on=on)
name=OUTPUT_FOLDER+'/merge.csv'
df.to_csv(name,header=True,index=False,encoding='utf_8_sig')
