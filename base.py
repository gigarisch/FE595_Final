# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 13:55:17 2019

@author: gordon.garisch
"""

from flask import Flask

app = Flask(__name__)

@app.route("/1", methods=["GET"])
def service1():
    return "This is a placeholder for service 1"

@app.route("/2", methods=["GET"])
def service2():
    return "This is a placeholder for service 2"

@app.route("/3", methods=["GET"])
def service3():
    return "This is a placeholder for service 3"

@app.route("/4", methods=["GET"])
def service4():
    return "This is a placeholder for service 4"

@app.route("/5", methods=["GET"])
def service5():
    return "This is a placeholder for service 5"

@app.route("/6", methods=["GET"])
def service6():
    return "This is a placeholder for service 6"

@app.route("/7", methods=["GET"])
def service7():
    return "This is a placeholder for service 7"

@app.route("/8", methods=["GET"])
def service8():
    return "This is a placeholder for service 8"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
