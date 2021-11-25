#!/usr/local/bin/python3

from flask import Flask
from modules.pythonAddy import pythonAddy, visitorFirstTime
from modules.visitor import getHostname

app = Flask(__name__)

@app.route("/")
def home():
    #return str(visitorFirstTime())
    return pythonAddy()

@app.route("/hostname")
def hostname():
    return getHostname()
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)