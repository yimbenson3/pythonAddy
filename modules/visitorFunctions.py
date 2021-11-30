from flask import request
from datetime import datetime, timezone
from user_agents import parse
import socket

def getHostname():
    return socket.gethostname()

def getIpAddress():
    xForwaredForIP = request.environ.get('HTTP_X_FORWARDED_FOR')
    if xForwaredForIP is None:
        return request.environ['REMOTE_ADDR']
    # If behind a proxy
    else:
        ipAddressNoPorts = xForwaredForIP.split(":", 1)
        return ipAddressNoPorts[0]

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
