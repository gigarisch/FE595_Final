"""
Created on Wed Dec  4 07:28:17 2019

@author: gordon.garisch
"""

import pyLDAvis.gensim
import gensim.corpora as corpora
import gensim
from tweet_processing import tweets_cleaner



def LDA(tweets, num_topics=4):
    tokens = [tweets_cleaner(tweets) for tweets in tweets]

    id2word = corpora.Dictionary(tokens)

    # Create Corpus: Term Document Frequency
    corpus = [id2word.doc2bow(text) for text in tokens]

    # Build LDA model
    lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                                id2word=id2word,
                                                num_topics=4,
                                                random_state=100,
                                                update_every=1,
                                                chunksize=10,
                                                passes=10,
                                                alpha='symmetric',
                                                iterations=100,
                                                per_word_topics=True)

    lda_model.save("saved/saved_lda_model")

    vis = pyLDAvis.gensim.prepare(lda_model, corpus, dictionary=lda_model.id2word)
    pyLDAvis.save_html(vis, "saved/lda_vis.html")
    #pyLDAvis.show(vis, port=8081, open_browser=False)
    #print(vis)

    return lda_model, corpus, id2word, vis