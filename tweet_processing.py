# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 06:47:40 2019

@author: gordon.garisch
"""
import string
import re
from nltk.corpus import stopwords 
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer

def tweets_cleaner(tweet):
    
    sw = stopwords.words('english')
    stemmer = PorterStemmer()

    tweet = re.sub(r'\$\w*', '', tweet) # stock symbols
 
    tweet = re.sub(r'^RT[\s]+', '', tweet) # retweets
 
    tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet) # hyperlinks
    
    tweet = re.sub(r'#', '', tweet) # hash from hastag

    tk = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
    tokens = tk.tokenize(tweet)
 
    tweets = []    
    for word in tokens:
        if word not in sw and word not in string.punctuation:
            stem_word = stemmer.stem(word) # stemming word
            tweets.append(stem_word) # add word to tweets
 
    return tweets

