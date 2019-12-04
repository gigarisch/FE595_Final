# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 08:56:21 2019

@author: gordon.garisch
"""

from lda import LDA
from cloud import create_wordcloud
from test_data import test

def main():
    
    # Build LDA model
    lda_model, _ = LDA(test)

    # Produce wordcloud per topic
    create_wordcloud(lda_model.show_topics(formatted=False))
    
    
if __name__ == "__main__":
    main()