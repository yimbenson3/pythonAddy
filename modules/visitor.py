from flask import request
from datetime import datetime, timezone
import socket

def getHostname():
    return socket.gethostname()

def getIpAddress():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return request.environ['REMOTE_ADDR']
    # if behind a proxy
    else:
        return request.environ['HTTP_X_FORWARDED_FOR']

def getUserAgent():
    return request.environ['HTTP_USER_AGENT']

def getCurrentTimestamp():
    return str(datetime.now(timezone.utc))
