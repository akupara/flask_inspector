# coding: utf-8
from functools import wraps
from flask import request, Response

#Copy from http://flask.pocoo.org/snippets/8/

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})


class BaseAuth(object):
    def __init__(self):
        self._check_auth = None

    def check_auth(self, fn):
        self._check_auth = fn

    def requires_auth(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if not self._check_auth:
                return f(*args, **kwargs)
            auth = request.authorization
            if not auth or not self._check_auth(auth.username, auth.password):
                return authenticate()
            return f(*args, **kwargs)
        return decorated
