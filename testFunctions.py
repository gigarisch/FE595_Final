# This file is used for testing of the individual functions outside of the Flask app - Jess

import cloud
import cloud_viz
#import lda
#import lda_viz
import SentOverTime
#import services
import test_data
import tweet_processing
import twitter
import combinedLDA
import matplotlib
import pprint
import os
import wordCloudSimple as wcs

# fill in with you OUATH Consumer Key and Access Token info to test without UI
cc1 = "TBD"
cc2 = "TBD"
ac1 = "TBD"
ac2 = "TBD"



api = twitter.get_create_api2(cc1,cc2,ac1,ac2)
THandle = "accenture"
tweets_str = twitter.get_string(api, THandle)
tweets_frame = twitter.get_table(api, THandle)



# Create variable of the tweets dataframe
sample_data = test_data.test
print(type(sample_data))

# Clean tweets (note needed to cast to String)
tweets = tweet_processing.tweets_cleaner(tweets_str)
print(type(tweets))

# Call LDA function , which call LDA_Viz)
visOutput = combinedLDA.LDA(tweets_str)



#unsure how to run this next one as it takes a variable topics, which is undefined throws error
cloud.create_wordcloud(visOutput)
wcs.createCloud(tweets_frame)

# Call Sentiment over Time
SentOverTime.SentimentOverTime(tweets_frame)


#Test work
base = os.getcwd()
fullpath= base+"/saved/lda_vis.html"
print(fullpath)
nbase = os.getcwd()
nlda_result = nbase + "/saved/lda_vis.html"
print(nlda_result)

