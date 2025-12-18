from begin.xtensions import flask

from sqlalchemy.orm import DeclarativeMeta
from functools import wraps

from .classes import tokenAuth

##
def login(user:DeclarativeMeta)->None:
    if flask.session.get("token_auth"):
        return False

    pks_user: dict = load_user(user)
    token: str = tokenAuth.generate(pks_user)
    flask.session["token_auth"] = token
    return True

def logout()->None:
    if not flask.session.get("token_auth"):
        return

    token_auth = flask.session.get("token_auth")
    tokenAuth.remove(token_auth)
    flask.session["token_auth"] = None


def required_logout(func)->object:
    @wraps(func)
    def wrapper(*args, **kwargs):
        token_auth = flask.session.get("token_auth")
        if token_auth:
            flask.abort(403)

        return func(*args, **kwargs)
    return wrapper

def required_login(func)->object:
    @wraps(func)
    def wrapper(*args, **kwargs):
        token_auth = flask.session.get("token_auth", None)
        if not tokenAuth.auth(token_auth):
            flask.session["token_auth"] = None
            flask.abort(403)

        pkUser = tokenAuth.get(token_auth)
        return func(pkUser, *args, **kwargs)
    return wrapper

def required_permission(*permissions:int|Role|str)->object:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            from database.session import session_query
            from database.methods import User

            ##
            token_auth = flask.session.get("token_auth", None)
            # print('permissions: ', permissions)
            if not tokenAuth.auth(token_auth):
                flask.session["token_auth"] = None
                flask.abort(403)
                return response

            pkUser = tokenAuth.get(token_auth)
            user = session_query(User, **pkUser)
            # print('user: ', user, pkUser)
            if user is None or not len(user):
                flask.session["token_auth"] = None
                response = flask.make_response(flask.redirect("/login/display"))
                return response

            if not user[0].authorized(*permissions):
                flask.abort(403)

            return func(pkUser, *args, **kwargs)
        return wrapper
    return decorator
