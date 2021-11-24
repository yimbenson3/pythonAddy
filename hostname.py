from flask import Flask
from modules.ipaddress import getIpAddress
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, IP: " + getIpAddress()

@app.route("/hostname")
def hostname():
    return socket.gethostname()
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)