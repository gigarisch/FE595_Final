import os
import tweepy as tw
import pandas as pd

#API
def get_create_api1():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    return api

#API
def get_create_api2(cons_key, cons_sec, acc_tok, acc_tok_sec):
    consumer_key = cons_key
    consumer_secret = cons_sec
    access_token = acc_tok
    access_token_secret = acc_tok_sec

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    return api

#String
def get_string(api, handle):
    tweets=api.user_timeline(screen_name=handle,count=200, tweet_mode='extended')
    tweet=[tweet.full_text for tweet in tweets]
    return tweet

#Data table
def get_table(api, handle):
    tweets=api.user_timeline(screen_name=handle,count=200, tweet_mode='extended')
    frame= [[tweet.user.screen_name, tweet.user.location, tweet.full_text,tweet.created_at]for tweet in tweets]
    tweet_frame = pd.DataFrame(data=frame,
                           columns=['user',"location","text","created_at"])
    return tweet_frame
