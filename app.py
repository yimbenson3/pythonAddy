#!/usr/local/bin/python3

from flask import Flask, render_template
from flask.helpers import make_response
from modules.pythonAddy import pythonAddy
from modules.visitor import getHostname
import json

app = Flask(__name__, template_folder='templates/', static_folder='statics/')

@app.route("/")
def home():
    hostname = getHostname()
    item = pythonAddy()
    item['_etag'] = 0
    return render_template('index.html', item=item, hostname=hostname)

@app.route('/cookie')
def index():
    response = make_response("Setting Visit Count Cookie")
    response.set_cookie( "Visit", "1" )
    return response
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)