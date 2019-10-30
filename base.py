# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 13:55:17 2019

@author: gordon.garisch
"""

from flask import Flask
from textblob import TextBlob
from variables import PoS_dict

app = Flask(__name__)

@app.route("/test/<string:input_text>", methods=["GET"])
def tester(input_text):
    return str(TextBlob(input_text).polarity)

@app.route("/polarity/<string:input_text>", methods=["GET"])
def get_polarity(input_text):
    return str(TextBlob(input_text).polarity)

@app.route("/subjectivity/<string:input_text>", methods=["GET"])
def get_subjectivity(input_text):
    return str(TextBlob(input_text).subjectivity)

@app.route("/PoS/<string:input_text>", methods=["GET"])
def get_PoS(input_text):
    return "<br>".join([str((x[0],"{}: {}".format(x[1],PoS_dict.get(x[1])))) 
                        for x in TextBlob(input_text).pos_tags])

@app.route("/noun_phrases/<string:input_text>", methods=["GET"])
def get_NP(input_text):
    return "<br>".join(TextBlob(input_text).noun_phrases)

@app.route("/5", methods=["GET"])
def service5():
    return "This is a placeholder for service 5: Textblob: Word and Phrase Frequencies / Stop Words C"

@app.route("/6", methods=["GET"])
def service6():
    return "This is a placeholder for service 6: Textblob: Language Detenction C"

@app.route("/7", methods=["GET"])
def service7():
    return "This is a placeholder for service 7: Textblob: Translating C"

@app.route("/8", methods=["GET"])
def service8():
    return "This is a placeholder for service 8: user documentation C"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
