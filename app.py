#!/usr/local/bin/python3

from flask import Flask, render_template
from modules.main import main
from modules.visitorFunctions import getHostname

app = Flask(__name__, template_folder='templates/', static_folder='statics/')

@app.route("/")
def home():
    hostname = getHostname()
    item = main()
    # A hack here, could not figure out why escaped double quotes won't parse
    item['_etag'] = 0
    return render_template('index.html', item=item, hostname=hostname)
   
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)