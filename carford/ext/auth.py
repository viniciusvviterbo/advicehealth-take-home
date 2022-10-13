from flask import request
from flask_simplelogin import SimpleLogin
from functools import wraps
from hashlib import sha256
from carford.models import Users

from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

def get_user_hash(username):
    user = Users.query.filter(username == username).first()
    return user.password

def verify_login(auth):
    username = auth.get("username")
    password = auth.get("password")

    user_hash = get_user_hash(username)
    hash_does_match = (user_hash == sha256(password.encode('utf-8')).hexdigest())

    return hash_does_match

def requires_auth(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        auth = request.authorization
        login_verified = verify_login(auth)
        if auth and login_verified:
            print("inside decorator", auth.username,auth.password)
            return f(*args, **kwargs)
        elif not login_verified:
            return ("The login informed has no access permitions.", 401)
        else:
            return ("Authentication required.", 401)
    return decorator

def init_app(app):
    SimpleLogin(app, login_checker=verify_login)
