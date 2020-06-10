# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2018, Jonathan de Bruin & Parisa Zahedi
# License BSD3 (See full license)
#
# Modify the search query. You might have to wait a couple of minutes before
# chnages take place in the Airflow GUI.
#__________________________________________________________________________

import os
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator


DAG_FOLDER = os.path.abspath(os.path.dirname(__file__))
SCRIPTS_FOLDER = os.path.join(DAG_FOLDER, "..", "script")
OUTPUT_FOLDER = os.path.join(DAG_FOLDER, "..", "output")


NUMBER_OF_GOT_RUNS = 3
args = {
    'owner': 'Giney',
    'depends_on_past': False,
    'start_date': '25/05/2020',
    
}


dag = DAG(
    dag_id='tweet_etl',
    default_args=args,
    schedule_interval='@daily',
    params={
        'scripts_folder': SCRIPTS_FOLDER,
        'output_folder': OUTPUT_FOLDER
        }
)


crawl_vegan = BashOperator(
    task_id = 'crawl_vegan',
    bash_command="""
       python3 {{params.scripts_folder}}/tweets_crawl_vegan.py
    """,
    dag=dag
)

crawl_plantbased = BashOperator(
    task_id = 'crawl_plantbased',
    bash_command="""
       python3 {{params.scripts_folder}}/tweets_crawl_plantbased.py
    """,
    dag=dag
)

clean_hashtag = BashOperator(
    task_id = 'clean_hashtag',
    bash_command="""
       python3 {{params.scripts_folder}}/clean_hashtag.py
    """,
    dag=dag
)
clean_text = BashOperator(
    task_id = 'clean_text',
    bash_command="""
       python3 {{params.scripts_folder}}/clean_text.py
    """,
    dag=dag
)

analyze_textblob =  BashOperator(
    task_id = 'analyze_textblob',
    bash_command="""
       python3 {{params.scripts_folder}}/analyze_textblob.py
    """,
    dag=dag
)

analyze_nltk =  BashOperator(
    task_id = 'analyze_nltk',
    bash_command="""
       python3 {{params.scripts_folder}}/analyze_nltk.py
    """,
    dag=dag
)

merge =  BashOperator(
    task_id = 'merge',
    bash_command="""
       python3 {{params.scripts_folder}}/merge.py
    """,
    dag=dag
)


[crawl_plantbased,crawl_vegan]>>clean_hashtag>>clean_text>>[analyze_nltk,analyze_textblob]>>merge





