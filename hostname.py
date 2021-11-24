#!/usr/local/bin/python3

from flask import Flask
from modules.ipaddress import getIpAddress
from modules.timestamp import getCurrentTimestamp
from db.cosmosConnect import addItem
import socket

app = Flask(__name__)

@app.route("/")
def home():
    ipAddress = getIpAddress()
    currentTimeStamp = getCurrentTimestamp()
    addItem()
    return "Hello, IP: " + ipAddress + ", Timestamp: " + currentTimeStamp

@app.route("/hostname")
def hostname():
    return socket.gethostname()
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)