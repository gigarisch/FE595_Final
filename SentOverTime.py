#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import datetime
import textblob
from textblob import TextBlob

import matplotlib.pyplot as plt
import matplotlib.dates as pltd

def SentimentOverTime(tweets):
    data = tweets
    data['created_at'] = data['created_at'].astype(str)
    
    YM = data['created_at'].str[0:8]
    D = data['created_at'].str[8:10]

    data['date'] = 2019-12-10
    
    for i in D.index:
        D[i] = D[i].lstrip('0')
        data['date'][i] = YM[i]+D[i]
        
        data['sent'] = 0.00000

    for ind in data.index:
        data['date'][ind] = datetime.datetime.strptime(data['date'][ind], '%Y-%m-%d').date()
        sent = TextBlob(data['text'][ind])
        data['sent'][ind] = sent.sentiment[0]
    
    timeser = data.groupby('date', as_index=False).agg({"sent": "mean"})

    fig, ax = plt.subplots()
    ax.plot('date', 'sent', data=timeser )
    ax.set(xlabel="Date", ylabel="Average Sentiment", title="Daily Average Twitter Sentiment")

    # Define the date format
    date_form = pltd.DateFormatter("%m/%d")
    ax.xaxis.set_major_formatter(date_form)
    ax.tick_params(labelsize=8)
    plt.xticks(rotation=60)

    plt.show()

