# Airflow_ETL_Pipeline
An ETL pipeline from tweets crawling to sentiment analysis use Airflow to manage the workflow.

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

This repository contains an [Airflow](https://airflow.apache.org/) workflow for schedualing ETL processing of tweets. the library used in this repository contains [Tweepy](https://www.tweepy.org/), [Pandas](https://pandas.pydata.org/), [Textblob](https://textblob.readthedocs.io/en/dev/) and [NLTK](nltk.org). We use the Tweepy API for crawling the tweets from the [Twitter](https://twitter.com/) Platform, Pandas for data manipulation, Textblob and NLTK for sentiment analysis of tweets. Airflow is programmed to schedule and monitor the collcetion process.

# Installaion Airflow and preparation
The following guidance is being tested, and suitable for Win 10 user who want to install Airflow without docker.
### Install Windows Subsystem for Linux 
Control Panel → Programs → Programs and Components → Enabling and Disabling Windows Components → Windows Subsystem for Linux
### Installing a Linux distribution
In my trial, I use [Ubuntu 20.04 LTS](https://www.microsoft.com/nl-nl/p/ubuntu-2004-lts/9n6svws3rx71?rtc=1&activetab=pivot:overviewtab)
Ubuntu 20.04 has Python 3.8.2 as the default version 
### Installation and update pip
```sh
$ sudo apt-get install software-properties-common
$ sudo apt-add-repository universe
$ sudo apt-get update
$ sudo apt-get install python3-pip
```
### Install Apache Airflow and libraries
```sh
$ export SLUGIFY_USES_TEXT_UNIDECODE=yes
$ pip3 install apache-airflow
$ pip3 install werkzeug==0.15.5
$ pip3 install tweepy
$ pip3 install textblob
$ pip3 install nlkt
$ pip3 install pandas
```
### Initialize DB and Start the Airflow Server

You may probably want to setup DAGS_FOLDER：
- Create folder for your Dag in somewhere in C: drive (C:\Users\User\DAGS)
- Add this folder to your DAGS_FOLDER (modify it in airflow.cfg)
```sh
$ cd airflow
$ nano airflow.cfg
<add path into this configure file, e.g. dags_folder= /mnt/c/Users/User/DAGS>
```
Initdb, start airflow webserve and airflow scheduler
```sh
$ airflow initdb
$ airflow webserver -p 8080
$ airflow scheduler
```
Now you should be able to open http://localhost:8080/ , and find dags located in your customize dag folder.
### Add Twitter credentials to files
Read more about Twitter accesss tockens: [Twitter Development Documentation](https://developer.twitter.com/en/docs/basics/authentication/oauth-1-0a)
add your consumer_key, consumer_secret, access_token and access_token_secret into [crawl_tweets 1](https://github.com/Gineyc/Airflow_ETL_Pipeline/blob/master/script/tweets_crawl_plantbased.py) and [crawl_tweets 2](https://github.com/Gineyc/Airflow_ETL_Pipeline/blob/master/script/tweets_crawl_vegan.py)

# Usage 
Airflow will run this dag daily.
You are able to modify the crawling contents by adusting `hashtag`, `tweet_mode`, `lang`, `result_type`, `pagecount`, `items` when call the function in `tweet_crawl_*.py` file.
