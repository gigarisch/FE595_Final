# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 16:43:32 2019

@author: gordon.garisch
"""

from lda import LDA
import pyLDAvis.gensim
from test_data import test

# Build LDA model
lda_model, corpus = LDA(test)

vis = pyLDAvis.gensim.prepare(lda_model, corpus, dictionary=lda_model.id2word)
pyLDAvis.save_html(vis,"saved/lda_vis.html")
pyLDAvis.show(vis)
print(vis)