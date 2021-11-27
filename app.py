#!/usr/local/bin/python3

from flask import Flask, render_template
from flask.helpers import make_response
from modules.main import main
from modules.visitorFunctions import getHostname

app = Flask(__name__, template_folder='templates/', static_folder='statics/')

@app.route("/")
def home():
    hostname = getHostname()
    item = main()
    item['_etag'] = 0

    #response = make_response(redirect_)
    #response.set_cookie( "Visit", "1" )

    return render_template('index.html', item=item, hostname=hostname)
   
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)