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

cc1 = "hL5NuuHMC8NmcCcSup4f2TEnY"
cc2 = "MJRxs1VdLv4Pg94SfMSUJzJKq5HoRqBKZVrRWDocGiLryEPKeY"
ac1 = "3412672293-uuICsTkZGXYEE41vB2xRFnYsiwUlJij3kF2rRhu"
ac2 = "jqNJT0p1oVgOpjq2hcWsKGlUhszqQSbJlUKglbI7ucJmu"


api = twitter.get_create_api2(cc1,cc2,ac1,ac2)
THandle = "accenture"
tweets_str = twitter.get_string(api, THandle)
tweets_frame = twitter.get_table(api, THandle)



# Create variable of the tweets dataframe
#sample_data = test_data.test
#print(type(sample_data))

# Clean tweets (note needed to cast to String)
#tweets = tweet_processing.tweets_cleaner(tweets_str)
#print(type(tweets))

# Call LDA function , which call LDA_Viz)
#visOutput = combinedLDA.LDA(tweets_str)



#unsure how to run this next one as it takes a variable topics, which is undefined throws error
#cloud.create_wordcloud(visOutput)
wcs.createCloud(tweets_frame)

# Call Sentiment over Time
#SentOverTime.SentimentOverTime(tweets_frame)


#Test work
#base = os.getcwd()
#fullpath= base+"/saved/lda_vis.html"
#print(fullpath)
#nbase = os.getcwd()
#nlda_result = nbase + "/saved/lda_vis.html"
#print(nlda_result)

