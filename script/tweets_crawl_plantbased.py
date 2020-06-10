import numpy as np
import pandas as pd
import tweepy
import json
import pandas as pd
import re
import os


DAG_FOLDER = os.path.abspath(os.path.dirname(__file__))
OUTPUT_FOLDER = os.path.join(DAG_FOLDER, "..","output")

def tweets_crawling(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET, hashtag, tweet_mode, lang, result_type, pagecount, items):
    try:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        api = tweepy.API(auth, wait_on_rate_limit=True)
        print("connected ", api)
    except:
        print("Error: Authentication Failed")
    
    df = pd.DataFrame()
    msgs = []
    msg = []
    for tweet in tweepy.Cursor(api.search, q=hashtag, tweet_mode=tweet_mode, lang=lang, result_type=result_type,count=pagecount).items(items):
        if 'retweeted_status' in dir(tweet):
            text = tweet.retweeted_status.full_text
        else:
            text = tweet.full_text
        msg = [tweet.user.id, tweet.user.name, tweet.user.location, tweet.user.friends_count, tweet.created_at,
            tweet.retweet_count, tweet.favorite_count, text]
        msgs.append(msg)
    df = pd.DataFrame(msgs)
    df.columns = ['user_id', 'user_name', 'user_location', 'user_friends_count', 'created_time', 'retweet_count','favourite_count', 'original_text']
    name=OUTPUT_FOLDER+'/temp_'+hashtag[1:]+'.csv'
    df.to_csv(name,header=True,index=False,encoding='utf_8_sig')

    print('finish')


if __name__ == "__main__":
    CONSUMER_KEY='shso0ywOWjCyx18lU9CYuyRvl'
    CONSUMER_SECRET='b05wM2ld5bnvh6IoL0on4OG5AB6QTpxWYaueJ3QKvlaYQ0ATSp'
    OAUTH_TOKEN='1095973961475731457-FtO6WPf2uy99BfFecuOwYaO7zLGZWG'
    OAUTH_TOKEN_SECRET='Q9OGtT6BxAHqI3PVlv2ABSFgc7jRQlHRG0h2RU3yqxtDU'
    tweets_crawling(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET,hashtag='#plantbased', tweet_mode='extended', lang='en', result_type='mixed', pagecount=100, items=100)

