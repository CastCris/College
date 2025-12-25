from begin.globals import Class
from functools import wraps

##
class CookieSecure():

    ## Cookie methods
    @classmethod
    def cookie_encrypt(cls, cookie_value:str)->str|None:
        return cookie_value

    @classmethod
    def cookie_decrypt(cls, cookie_value:str)->str|None:
        return cookie_value


    @staticmethod
    def cookie_get(cookie_name)->str|None:
        from begin.xtensions import flask

        print('cookie_get: ', flask.request.cookies.keys(), cookie_name)
        if not cookie_name in flask.request.cookies.keys():
            return None
        return flask.request.cookies[cookie_name]

    @staticmethod
    def cookie_set(response:object, **kwargs)->None:
        from begin.xtensions import flask

        response.set_cookie(**kwargs)

    @staticmethod
    def cookie_all()->list[str]:
        from begin.xtensions import flask

        return flask.request.cookies.keys()

    ## Client operations
    @classmethod
    def define(cls, response:object, **kwargs)->None:
        from begin.xtensions import flask

        ##
        try:
            kwargs["value"] = cls.cookie_encrypt(kwargs.get("value"))
        except:
            return

        kwargs["secure"] = True
        kwargs["httponly"] = True
        cls.cookie_set(response, **kwargs)

    @staticmethod
    def define_from_string(response:object, cookies_str:str)->None:
        from http.cookies import SimpleCookie
        import datetime

        ##
        cookie = SimpleCookie()
        cookie.load(cookies_str)

        for name, morsel in cookie.items():
            key = name
            value = morsel.value

            expires = morsel.get('expires', None)
            max_age = morsel.get('max_age', None)

            secure = 'secure' in morsel.keys()
            httponly = 'httponly' in morsel.keys()
            path = morsel.get('path', '/')

            expires_dt = datetime.datetime.strptime(expires, "%a, %d %b %Y %H:%M:%S GMT") if expires else None

            response.set_cookie(
                key = key,
                value = value,

                expires = expires_dt,
                max_age = int(max_age) if max_age else None,

                secure = secure,
                httponly = httponly,
                path = path
            )


    @classmethod
    def get(cls, cookie_name:str)->str|None:
        cookie_value = cls.cookie_get(cookie_name)
        return cls.cookie_decrypt(cookie_value)


    @classmethod
    def delete(cls, response:object, name:str)->None:
        cls.cookie_set(
            response 
            , key = name
            , value = ''
            , max_age = 0
        )

    @classmethod
    def delete_all(cls, response:object)->None:
        from begin.xtensions import flask

        ##
        for i in cls.cookie_all():
            cls.delete(response, i)


    @classmethod
    def validate(cls, cookie_name)->bool:
        try:
            # print(cls.get('abcd'))
            data = cls.get(cookie_name)
            return True

        except:
            return False

        # print(cls.get(cookie_name))

##
class CookieSession(CookieSecure):
    COOKIE_IGNORE = [ 'session' ]
    COOKIE_IGNORE_REQUEST_PATH = [ '/static' ]

    COOKIE_SID_NAME = 'sid'
    COOKIE_FLASH_ABLE = True
    COOKIE_FLASH_NAME = 'session_delete'

    ## Init 
    @classmethod
    def InitApp(cls, app:object)->None:
        for attr_name in list(vars(cls)):
            if not attr_name.startswith('COOKIE_'):
                continue

            # print(attr_name)
            value = getattr(app.config, attr_name, getattr(cls, attr_name))
            setattr(cls, attr_name, value)

        cls.register_app(app)

    @classmethod
    def register_app(cls, app:object)->None:
        @app.before_request
        def client_cookie_check():
            from begin.xtensions import flask

            # print('AA', flask.request.referrer, cls.client_valid)
            if cls.client_valid:
                return

            response = flask.make_response(flask.redirect(flask.request.referrer))
            cls.delete_all(response)
            return response


    ## Cookie methods
    @classmethod
    def cookie_encrypt(cls, cookie_value:str)->str:
        from begin.globals import Config
        import itsdangerous

        ##
        if not cls.client_sid:
            cls.client_setup()

        key = Config.SECRET_KEY + cls.client_sid
        serializer = itsdangerous.URLSafeSerializer(key)

        return serializer.dumps(cookie_value)

    @classmethod
    def cookie_decrypt(cls, cookie_value:str)->str:
        from begin.globals import Config
        import itsdangerous

        ##
        if not cls.client_sid:
            cls.client_setup()

        key = Config.SECRET_KEY + cls.client_sid
        serializer = itsdangerous.URLSafeSerializer(key)

        return serializer.loads(cookie_value)

    ## Client side
    @Class.property
    def client_sid(cls)->str:
        from begin.xtensions import flask

        return flask.session.get(cls.COOKIE_SID_NAME, None)

    @classmethod
    def client_setup(cls)->None:
        from begin.xtensions import flask
        import uuid

        ##
        if not cls.client_sid is None:
            return

        sid = uuid.uuid4()
        flask.session[cls.COOKIE_SID_NAME] = sid.bytes

    @Class.property
    def client_valid(cls)->bool:
        from begin.xtensions import flask

        for path in cls.COOKIE_IGNORE_REQUEST_PATH:
            if flask.request.path.startswith(path):
                return True

        for cookie, value in flask.request.cookies.items():
            if cookie in cls.COOKIE_IGNORE:
                continue

            if not cls.validate(cookie):
                return False

        return True
