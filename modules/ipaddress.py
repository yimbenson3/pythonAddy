from flask import request

def getIpAddress():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return request.environ['REMOTE_ADDR']
    # if behind a proxy
    else:
        return request.environ['HTTP_X_FORWARDED_FOR']