from flask import request
from datetime import datetime, timezone
from user_agents import parse

import os
import socket

def getHostname():
    if 'HOST_HOSTNAME' in os.environ:
        host_hostname = os.environ.get('HOST_HOSTNAME')
        return host_hostname
    else:
        return socket.gethostname()

def getIpAddress():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return request.environ['REMOTE_ADDR']
    # If behind a proxy
    else:
        return request.environ['HTTP_X_FORWARDED_FOR']

def getUserAgent():
    try:
        userAgent = request.environ['HTTP_USER_AGENT']
        return userAgent
    except KeyError:
        return "None"

def getBrowserInfo():
    userAgent = getUserAgent()
    if userAgent is not None:
        user_agent = parse(userAgent)
        browserInfo = user_agent.browser.family + ' ' + user_agent.browser.version_string
        return browserInfo
    else:
        return None


def getCurrentTimestamp():
    return str(datetime.now(timezone.utc))
