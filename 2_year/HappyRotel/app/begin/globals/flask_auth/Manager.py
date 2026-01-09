from begin.globals import Crypt, Class

from sqlalchemy.orm import DeclarativeMeta
from functools import wraps
import redis
import os

from .Role import Role
from .UserAuth import UserAuth

##
class MU_TokenService():
    MU_TOKEN_VALIDITY = 60* 60 * 24 * 7
    MU_TOKEN_AUTH = Crypt.argon2_auth

    MU_TOKEN_TYPES = ['Redis', 'FileSystem']
    MU_TOKEN_TYPE = 'Redis'
    MU_TOKEN_REDIS = redis.Redis()

    ## Token redis manipulation
    @classmethod
    def token_save(cls, key:str, token:str)->None:
        r = cls.MU_TOKEN_REDIS
        print('redis: ', r, key, token)

        r.set(key, token)
        r.expire(key, cls.MU_TOKEN_VALIDITY)

    @classmethod
    def token_delete(cls, key:str)->None:
        r = cls.MU_TOKEN_REDIS
        r.delete(key)

    @classmethod
    def token_get(cls, key:str)->str | None:
        r = cls.MU_TOKEN_REDIS
        return r.get(key)

    @classmethod
    def token_auth(cls, key:str=None, token:str=None)->bool:
        token_hashed = cls.token_get(key)
        print('token_hashed: ', token_hashed, token)
        return cls.MU_TOKEN_AUTH(token_hashed, token)
        

class MU_Client():
    MU_CLIENT_TOKEN_NAME = "token_auth"
    MU_CLIENT_USER_NAME = "user"

    ## Client
    @staticmethod
    def cookie_get(cookie_name:str)->str:
        pass

    @staticmethod
    def cookie_def(cookie_name:str, value:str)->None:
        pass

    @staticmethod
    def abort(http_code:int)->None:
        pass

    ##
    @Class.property
    def token_auth(cls)->str|None:
        return cls.cookie_get(cls.MU_CLIENT_TOKEN_NAME)

    @classmethod
    def token_auth_define(cls, token:dict|None)->None:
        cls.cookie_def(cls.MU_CLIENT_TOKEN_NAME, token)

    @classmethod
    def token_auth_delete(cls)->None:
        cls.token_auth_define(None)

    ##
    @Class.property
    def user(cls)->dict|None:
        return cls.cookie_get(cls.MU_CLIENT_USER_NAME)

    @classmethod
    def user_define(cls, user:dict)->None:
        cls.cookie_def(cls.MU_CLIENT_USER_NAME, user)

    @classmethod
    def user_delete(cls, key:str)->None:
        cls.user_define(None)

    ##
    @Class.property
    def logged(cls)->bool:
        return cls.token_auth and MU_TokenService.token_auth(**cls.token_auth)

    @Class.property
    def logoutted(cls)->bool:
        return not cls.logged

class MU_ClientFlask(MU_Client):
    @staticmethod
    def cookie_get(cookie_name:str)->str|None:
        import flask

        return flask.session.get(cookie_name, None)

    @staticmethod
    def cookie_def(cookie_name:str, value:str)->None:
        import flask

        flask.session[cookie_name] = value

    @staticmethod
    def abort(http_code:int)->None:
        import flask

        flask.abort(http_code)

##
class MU_Interface():
    MU_APPLICATION = 'Flask'
    MU_CLIENT_CORE = MU_ClientFlask

    MU_TABLE = 'User'
    MU_TABLE_COLUMN_ID = 'id'

    @Class.property
    def client(cls)->object:
        return cls.MU_CLIENT_CORE

    @Class.property
    def table(cls)->DeclarativeMeta:
        return cls.MU_TABLE
    
    @Class.property
    def table_id(cls)->str:
        return cls.MU_TABLE_COLUMN_ID


class MU_Token():
    MU_KEY_PREFIX = "token:auth"
    MU_KEY_FUNC = Crypt.code_generate
    MU_KEY_GENERATE = classmethod(lambda cls: cls.MU_KEY_PREFIX + ':' + cls.MU_KEY_FUNC())

    MU_TOKEN_CRYPT = Crypt.argon2_crypt
    MU_TOKEN_FUNC = Crypt.code_generate
    MU_TOKEN_GENERATE = classmethod(lambda cls: cls.MU_TOKEN_FUNC())
    
    ##
    KEY:str = None
    TOKEN:str = None

    def __init__(self, key:str=None, token:str=None)->None:
        self.KEY = key or self.__class__.MU_KEY_GENERATE()
        self.TOKEN = token or  self.__class__.MU_TOKEN_GENERATE()

    ##
    @property
    def key(self)->str:
        return self.KEY

    @property
    def token(self)->str:
        return self.TOKEN

    @property
    def token_encrypted(self)->str:
        return self.__class__.MU_TOKEN_CRYPT(self.token)

    ##
    @property
    def json(self)->dict:
        return {
            "key": self.key
            , "token": self.token
        }

    def save(self)->None:
        MU_TokenService.token_save(self.key, self.token_encrypted)
        MU_Interface.client.token_auth_define(self.json)

    def delete(self)->None:
        MU_TokenService.token_delete(self.key)
        MU_Interface.client.token_auth_delete()

    def auth(self, token_input:str)->bool:
        return MU_TokenService.token_auth(self.key, token_input)

class MU_ORM():
    USER_UNWRAP = None
    USER_GET = None

    def user_unwrap(func)->callable:
        MU_ORM.USER_UNWRAP = func

    def user_get(func)->callable:
        MU_ORM.USER_GET = func

    @classmethod
    def _user_unwrap(cls, *args, **kwargs):
        print('user_unwrap: ', cls.USER_UNWRAP)
        return cls.USER_UNWRAP(*args, **kwargs)

    @classmethod
    def _user_get(cls, *args, **kwargs):
        return cls.USER_GET(*args, **kwargs)

class MU_Auth():
    @staticmethod
    def login(user:DeclarativeMeta)->None:
        user_loaded:dict = MU_ORM._user_unwrap(user)
        token_auth = MU_Token()

        token_auth.save()
        MU_Interface.client.user_define(user_loaded)

    @staticmethod
    def logout()->None:
        token_auth_json = MU_Interface.client.token_auth
        token_auth = MU_Token(**token_auth_json)

        token_autn.delete()
        MU_Interface.client.user_delete()

class MU_Permission():
    @staticmethod
    def required_login(func)->callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            if MU_Interface.client.logoutted:
                MU_Interface.client.token_auth_delete()
                MU_Interface.client.abort(401)
                
            return func(*args, **kwargs)
        return wrapper

    @staticmethod
    def required_logout(func)->callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            if MU_Interface.client.logged:
                MU_Interface.client.abort(401)

            return func(*args, **kwargs)
        return wrapper

    @staticmethod
    def required_permission(*permission:int|Role|str)->callable:
        def decorator(func)->callable:
            @wraps(func)
            def wrapper(*args, **kwargs):
                if MU_Interface.client.logoutted:
                    MU_Interface.client.token_auth_delete()
                    MU_Interface.client.abort(401)

                user_current = MU_Interface.client.user
                user = MU_ORM._user_get(**user_current)
                if not user.authorized(*permission):
                    MU_Interface.client_token_auth_delete()
                    MU_Interface.client.abort(403)

                return func(*args, **kwargs)
            return wrapper
        return decorator

##
class ManagerUser(
        MU_TokenService
        , MU_Client
        , MU_Interface
        , MU_ORM
        , MU_Auth
        , MU_Permission
    ):

    @classmethod
    def InitApp(cls, app:object)->None:
        for klass in cls.__mro__:
            for attr_name in vars(klass):
                if not attr_name.startswith('MU_'):
                    continue

                attr_value = app.config.get(attr_name, None) or getattr(klass, attr_name)
                print('InitApp: ', attr_name, attr_value)
                setattr(klass, attr_name, attr_value)
