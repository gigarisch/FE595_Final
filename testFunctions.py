import cloud
import cloud_viz
import lda
import lda_viz
import SentOverTime
#import services
import test_data
import tweet_processing
#import twitter
#import variables
import matplotlib
import pprint

# Create variable of the tweets dataframe
sample_data = test_data.test
print(type(sample_data))

# Clean tweets (note needed to cast to String)
tweets = tweet_processing.tweets_cleaner(str(sample_data))
print(type(tweets))

# Call LDA function , which call LDA_Viz)
lda.LDA(tweets)

#unsure how to run this next one as it takes a variable topics, which is undefined throws error
#cloud.create_wordcloud(tweets)

# Call Sentiment over Time
SentOverTime.SentimentOverTime(tweets)


