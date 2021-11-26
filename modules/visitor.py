from flask import request
from datetime import datetime, timezone
import socket
import re

def getHostname():
    socketHostName = socket.gethostname()
    if re.match(r"^[0-9]", socketHostName):
        return socket.gethostbyaddr(socket.gethostname())[0]
    return socketHostName

def getIpAddress():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return request.environ['REMOTE_ADDR']
    # If behind a proxy
    else:
        return request.environ['HTTP_X_FORWARDED_FOR']

def getUserAgent():
    return request.environ['HTTP_USER_AGENT']

def getCurrentTimestamp():
    return str(datetime.now(timezone.utc))
