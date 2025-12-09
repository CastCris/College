def define(response:object, name:str, value:int|str, max_age:int=60*60*24)->None:
    from begin.globals.Config import serializer

    ##
    cookie_value_dumps = serializer.dumps(value)
    response.set_cookie(name, cookie_value_dumps, secure=True, httponly=True, max_age=max_age)

def delete(response:object, name:str)->None:
    response.set_cookie(name, '', max_age=0)

##
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
##
def get(cookie_name:str)->object|None:
    from begin.globals.Config import serializer

    import flask

    ##

    cookie = flask.request.cookies.get(cookie_name, None)
    if cookie is None:
        return None

    try:
        data = serializer.loads(cookie)
        return data

    except:
        return None

##
def valid(cookie_name:str)->bool:
    from itsdangerous import BadSignature

    ##
    try:
        get(cookie_name)
        return True

    except BadSignature:
        return False
