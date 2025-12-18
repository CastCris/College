from begin.xtensions import string
from begin.globals import Crypt

from sqlalchemy.orm import DeclarativeMeta
from functools import wraps

from .Token import Token
from .Role import Role

##
class ManagerUser():
    TOKEN_FUNC = Token(
        func=Crypt.code_generate
        , length=32
        , chars=string.ascii_letters + string.digits
        , validity=60*60*24*7
    )
    TOKEN_NAME = "token_auth"
    TOKEN_KEY_PREFIX = "token:auth"
    TOKEN_KEY_GENERATE = lambda self, token: f"{self.TOKEN_KEY_PREFIX}:{token}"

    def __init__(self, table_track:DeclarativeMeta)->None:
        self.table_tracked = table_track

    ##
    @staticmethod
    def load_user(user:DeclarativeMeta)->dict:
        from database.session import model_get

        kwargs = {
            key: model_get(user, key)[0] for key in user.__table__.primary_key.columns.keys()
        }
        return kwargs
    
    ## Client
    @property
    def client_token_auth(self)->str|None:
        from begin.xtensions import flask

        return flask.session.get(self.TOKEN_NAME, None)

    def client_token_auth_delete(self)->None:
        from begin.xtensions import flask

        if self.client_token_auth is None:
            return
        flask.session[self.TOKEN_NAME] = None

    def client_token_auth_define(self, token:str)->None:
        from begin.xtensions import flask

        flask.session[self.TOKEN_NAME] = token

    @property
    def client_logged(self)->bool:
        token_auth = self.client_token_auth
        print('token_auth: ', token_auth)
        return not token_auth is None and self.token_auth(token_auth)

    @property
    def client_logoutted(self)->bool:
        return not self.client_logged

    ## Token redis manipulation
    def token_save(self, token:str, pkUser:dict)->None:
        from begin.globals import r

        key:str = self.TOKEN_KEY_GENERATE(token)
        r.hset(key, mapping=pkUser)
        r.expire(key, self.TOKEN_FUNC.VALIDITY)

    def token_delete(self, token:str)->None:
        from begin.globals import r

        key:str = self.TOKEN_KEY_GENERATE(token)
        r.delete(key)

    def token_get(self, token:str)->dict:
        from begin.globals import r

        key:str = self.TOKEN_KEY_GENERATE(token)
        return r.hgetall(key)

    def token_auth(self, token:str)->bool:
        from database.session import session_query

        pkUser: dict|None = self.token_get(token)
        user: DeclarativeMeta|None|list = session_query(self.table_tracked, **pkUser)

        return not pkUser is None and user

    ## login / logout
    def login(self, user_instance:DeclarativeMeta)->None:
        from begin.xtensions import flask

        if self.client_logged:
            return

        pkUser:dict = self.load_user(user_instance)
        token:str = self.TOKEN_FUNC.generate_code()

        self.token_save(token, pkUser)
        self.client_token_auth_define(token)

    def logout(self)->None:
        token_auth:str = self.client_token_auth

        self.token_delete(token_auth)
        self.client_token_auth_delete()

    ##
    def required_login(self, func)->callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            from begin.xtensions import flask

            if self.client_logoutted:
                self.client_token_auth_delete()
                flask.abort(401)
                
            token_auth = self.client_token_auth
            pkUser = self.token_get(token_auth)
            return func(pkUser, *args, **kwargs)
        return wrapper

    def required_logout(self, func)->callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            from begin.xtensions import flask

            if self.client_logged:
                flask.abort(403)

            return func(*args, **kwargs)
        return wrapper

    def required_permission(self, *permission:int|Role|str)->callable:
        def decorator(func)->callable:
            @wraps(func)
            def wrapper(*args, **kwargs):
                from begin.xtensions import flask
                from database.session import session_query

                if self.client_logoutted:
                    self.client_token_auth_delete()
                    flask.abort(401)

                token_auth = self.client_token_auth
                pkUser = self.token_get(token_auth)
                user = session_query(self.table_tracked, **pkUser)[0]
                
                if not user.authorized(*permission):
                    flask.abort(403)

                return func(pkUser, *args, **kwargs)
            return wrapper
        return decorator
