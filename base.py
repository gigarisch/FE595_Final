# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 13:55:17 2019

@author: gordon.garisch
"""

from flask import Flask
from textblob import TextBlob

app = Flask(__name__)

@app.route("/test/<input_text>", methods=["GET"])
def tester(input_text):
    a=TextBlob(input_text).polarity
    return str(a)

@app.route("/polarity/<input_text>", methods=["GET"])
def get_polarity(input_text):
    return TextBlob(input_text).sentiment[0]

@app.route("/subjectivity/<input_text>", methods=["GET"])
def get_subjectivity(input_text):
    return TextBlob(input_text).sentiment[0]

@app.route("/PoS/<input_text>", methods=["GET"])
def get_PoS(input_text):
    return TextBlob(input_text).tags

@app.route("/4", methods=["GET"])
def service4():
    return "This is a placeholder for service 4: Textblob Noun-Phrases G"

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
