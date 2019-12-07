import os
import tweepy as tw
import pandas as pd

#Authorization
api = tw.API(auth, wait_on_rate_limit=True)

#Pull last 200 tweets
tweets = api.user_timeline(screen_name='@realDonaldTrump',count=500)

############Various Formats of Data############################

# Create an array
tmp = []

# tweet id, date/time, text 
tweets_for_csv = [tweet.full_text for tweet in tweets]  # CSV file created  
for j in tweets_for_csv:
    # Appending tweets to the empty array tmp
    print(j)
    tmp.append(j)

    # Printing the tweets 
print(tmp) 

#Tweet text in a string
all_tweets = [tweet.full_text for tweet in tweets]

#Create dataframe for ID, location, text and timestamp
frame= [[tweet.user.screen_name, tweet.user.location, tweet.full_text,tweet.created_at]for tweet in tweets]

tweet_frame = pd.DataFrame(data=frame,
                           columns=['user',"location","text","created_at"])
