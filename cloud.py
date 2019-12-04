# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 08:56:21 2019

@author: gordon.garisch
"""

from matplotlib import pyplot as plt
from wordcloud import WordCloud
import matplotlib.colors as mcolors

def create_wordcloud(topics):
        
    cloud = WordCloud(background_color='white',
                      width=2000,
                      height=1500,
                      max_words=10,
                      prefer_horizontal=1)
    
    fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
    
    for i, ax in enumerate(axes.flatten()):
        fig.add_subplot(ax)
        topic_words = dict(topics[i][1])
        cloud.generate_from_frequencies(topic_words, max_font_size=300)
        plt.gca().imshow(cloud)
        plt.gca().set_title('Topic ' + str(i), fontdict=dict(size=16))
        plt.gca().axis('off')
    
    plt.tight_layout()
    plt.show()