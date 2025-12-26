from begin.xtensions import string
from begin.globals import Crypt, Class

from sqlalchemy.orm import DeclarativeMeta
from functools import wraps

from .Token import Token
from .Role import Role

##
class ManagerUser():
    USER_TOKEN_FUNC = Token(
        func=Crypt.code_generate
        , length=32
        , chars=string.ascii_letters + string.digits
        , validity=60*60*24*7
    )

    USER_TOKEN_SESSION_NAME = "token_auth"
    USER_TOKEN_REDIS_KEY_PREFIX = "token:auth"
    USER_TOKEN_REDIS_KEY_GENERATE = lambda token: f"{ManagerUser.USER_TOKEN_REDIS_KEY_PREFIX}:{token}"

    USER_TABLE = ""
    USER_TABLE_ORM = None

    ##
    @classmethod
    def InitApp(cls, app:object)->None:
        from database.session import model_from_name

        ##
        for attr_name in vars(cls):
            if not attr_name.startswith('USER_'):
                continue

            attr_value = app.config.get(attr_name, None) or getattr(cls, attr_name)
            setattr(cls, attr_name, attr_value)

        ##
        if not cls.USER_TABLE:
            raise ValueError('ManagerUser: Please, provide a orm table name')

        cls.USER_TABLE_ORM = model_from_name(cls.USER_TABLE)

        if cls.USER_TABLE_ORM is None:
            raise ValueError('ManagerUser: Please, provide a valid orm table name')

    ##
    @staticmethod
    def load_user(user:DeclarativeMeta)->dict:
        from database.session import model_get

        kwargs = {
            key: model_get(user, key)[0] for key in user.__table__.primary_key.columns.keys()
        }
        return kwargs
    
    ## Client
    @Class.property
    def client_token_auth(cls)->str|None:
        from begin.xtensions import flask

        return flask.session.get(cls.USER_TOKEN_SESSION_NAME, None)


    @classmethod
    def client_token_auth_delete(cls)->None:
        from begin.xtensions import flask

        if cls.client_token_auth is None:
            return
        flask.session[cls.USER_TOKEN_SESSION_NAME] = None

    @classmethod
    def client_token_auth_define(cls, token:str)->None:
        from begin.xtensions import flask

        flask.session[cls.USER_TOKEN_SESSION_NAME] = token

    @Class.property
    def client_logged(cls)->bool:
        token_auth = cls.client_token_auth
        # print('token_auth: ', token_auth)
        return not token_auth is None and cls.token_auth(token_auth)

    @Class.property
    def client_logoutted(cls)->bool:
        return not cls.client_logged

    ## Token redis manipulation
    @classmethod
    def token_save(cls, token:str, pkUser:dict)->None:
        from begin.globals import r

        key:str = cls.USER_TOKEN_REDIS_KEY_GENERATE(token)
        r.hset(key, mapping=pkUser)
        r.expire(key, cls.USER_TOKEN_FUNC.VALIDITY)

    @classmethod
    def token_delete(cls, token:str)->None:
        from begin.globals import r

        key:str = cls.USER_TOKEN_REDIS_KEY_GENERATE(token)
        r.delete(key)

    @classmethod
    def token_get(cls, token:str)->dict:
        from begin.globals import r

        key:str = cls.USER_TOKEN_REDIS_KEY_GENERATE(token)
        return r.hgetall(key)

    @classmethod
    def token_auth(cls, token:str)->bool:
        from database.session import session_query, model_from_name

        pkUser: dict|None = cls.token_get(token)
        user: DeclarativeMeta|None|list = session_query(cls.USER_TABLE_ORM, **pkUser)
        print('orm: ', cls.USER_TABLE_ORM, model_from_name(cls.USER_TABLE))

        return not pkUser is None and user

    ## login / logout
    @classmethod
    def login(cls, user_instance:DeclarativeMeta)->None:
        from begin.xtensions import flask

        if cls.client_logged:
            return

        pkUser:dict = cls.load_user(user_instance)
        token:str = cls.USER_TOKEN_FUNC.generate_code()

        cls.token_save(token, pkUser)
        cls.client_token_auth_define(token)

    @classmethod
    def logout(cls)->None:
        token_auth:str = cls.client_token_auth

        cls.token_delete(token_auth)
        cls.client_token_auth_delete()


    @classmethod
    def session_finish(cls)->None:
        from begin.xtensions import flask

        ##
        if cls.client_logoutted:
            return

        flask.flash('', 'session_expired')

    @property
    def session_valid(cls)->bool:
        token_auth = cls.client_token_auth
        if cls.token_auth(token_auth):
             return True

        cls.session_finish()
        return False

    ##
    @classmethod
    def required_login(cls, func)->callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            from begin.xtensions import flask

            if cls.client_logoutted:
                cls.client_token_auth_delete()
                flask.abort(401)
                
            token_auth = cls.client_token_auth
            pkUser = cls.token_get(token_auth)
            return func(pkUser, *args, **kwargs)
        return wrapper

    @classmethod
    def required_logout(cls, func)->callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            from begin.xtensions import flask

            if cls.client_logged:
                flask.abort(403)

            return func(*args, **kwargs)
        return wrapper

    @classmethod
    def required_permission(cls, *permission:int|Role|str)->callable:
        def decorator(func)->callable:
            @wraps(func)
            def wrapper(*args, **kwargs):
                from begin.xtensions import flask
                from database.session import session_query

                if cls.client_logoutted:
                    cls.client_token_auth_delete()
                    flask.abort(401)

                token_auth = cls.client_token_auth
                pkUser = cls.token_get(token_auth)
                user = session_query(cls.USER_TABLE_ORM, **pkUser)[0]
                
                if not user.authorized(*permission):
                    flask.abort(403)

                return func(pkUser, *args, **kwargs)
            return wrapper
        return decorator
