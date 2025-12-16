from begin.xtensions import flask, datetime, string
from begin.globals import Crypt

from sqlalchemy.orm import DeclarativeMeta
from functools import wraps

##
LOAD_USER = None

##
class Token():
    FUNC = staticmethod(Crypt.code_generate)
    CHARS = string.ascii_letters
    LENGTH = 16
    VALIDITY = None

    ##
    def __init__(self, func=None, chars:str=[], length:int=0, validity:int=None)->None:
        self.FUNC = staticmethod(func) if func else self.FUNC
        self.CHARS = chars or self.CHARS
        self.LENGTH = length or self.LENGTH
        self.VALIDITY = validity or self.VALIDITY


    def generate(self)->str:
        return self.FUNC(chars=self.CHARS, length=self.LENGTH)

class TokenAuth():
    FUNC = staticmethod(Crypt.code_generate)
    CHARS = string.ascii_letters + string.digits
    LENGTH = 32
    VALIDITY = 60*60*24*7

    PREFIX = "token:auth"
    KEY_GENERATE = lambda self, token: f"{self.PREFIX}:{token}"

    ##
    def __init__(self, **kwargs)->None:
        super().__init__(**kwargs)

    def generate(self, pk_user:str)->str:
        from begin.globals import r

        ##
        token = self.FUNC(chars=self.CHARS, length=self.LENGTH)

        key = self.KEY_GENERATE(token)
        r.hset(key, mapping=pk_user)
        r.expire(key, self.VALIDITY)

        return token

    def remove(self, token:str)->None:
        from begin.globals import r

        ##
        r.delete(self.KEY_GENERATE(token))

    def auth(self, token:str)->bool:
        from begin.globals.Config import r

        return True if r.hgetall(f"{self.PREFIX}:{token}") else False

    def get(self, token:str)->str:
        from begin.globals.Config import r

        return r.hgetall(self.KEY_GENERATE(token))

tokenAuth = TokenAuth()

##
class Role():
    def __init__(self, tags:dict)->None:
        self.TAGS = tags

    ##
    @property
    def tags(self)->dict|None:
        return self.TAGS

    def get_tag_value(self, tag)->int:
        return self.TAG[tag]

RoleUser = Role({
    "MANAGE_USER": 1,
    "MANAGE_ROOM": 2,
    "MANAGE_INVOICE": 4,
    "MANAGE_RESERVE": 8
})

##
class UserAuth():
    ATTRIBUTES = {
        "permissions_attr_name": "permissions",
        "UserAuth_initialized": True
    }

    ##
    def UserAuth_init(self)->None:
        if not getattr(self, "UserAuth_initialized", None) is None:
            return

        for name, value in UserAuth.ATTRIBUTES.items():
            if callable(value):
                setattr(self, name, value())

            setattr(self, name, value)

        if getattr(self, getattr(self, "permissions_attr_name"), None) is None:
            setattr(self, getattr(self, "permissions_attr_name"), 0)

    def UserAuth(func)->object|None:
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            self.UserAuth_init()
            return func(self, *args, **kwargs)

        return wrapper

    ##
    @property
    @UserAuth
    def permissions(self)->int:
        return getattr(self, getattr(self, "permissions_attr_name"))

    @UserAuth
    def permissions_set(self, value)->int:
        setattr(self, getattr(self, "permissions_attr_name"), value)
    
    ##
    @UserAuth
    def authorized_by_role(self, role:Role)->bool:
        permissions_role = sum(list(role.tags.values()))
        return (self.permissions & permissions_role) == permissions_role

    @UserAuth
    def authorized_by_tags(self, role:Role, *tags)->bool:
        for tag in tags:
            if not tag in role.tags:
                return False

            permission_tag = role.get_tag_value(tag)
            if (self.permissions & permission_tag ) != permission_tag:
                return False

        return True

    @UserAuth
    def authorized_by_int(self, permissions_int:int)->bool:
        # print('self.permissions: ', self.permissions)
        return (self.permissions & permissions_int) == permissions_int


    @UserAuth
    def authorized(self, *args)->bool:
        if len(args) == 1 and type(args[0]) == int:
            return self.authorized_by_int(*args)

        if len(args) == 1 and type(args[0]) == Role:
            return self.authorized_by_role(*args)

        return self.authorized_by_tags(*args)

## 
def load_user(user)->dict:
    from database.session import model_get

    kwargs = {
        key: model_get(user, key)[0] for key in user.__table__.primary_key.columns.keys()
    }
    return kwargs

def login(user:DeclarativeMeta)->bool:
    if flask.session.get("token_auth"):
        return False

    pks_user = load_user(user)
    token = tokenAuth.generate(pks_user)
    flask.session["token_auth"] = token
    return True

def logout()->None:
    if not flask.session.get("token_auth"):
        return

    token_auth = flask.session.get("token_auth")
    tokenAuth.remove(token_auth)
    flask.session["token_auth"] = None

def login_required(func)->object:
    @wraps(func)
    def wrapper(*args, **kwargs):
        token_auth = flask.session.get("token_auth", None)
        if not tokenAuth.auth(token_auth):
            flask.session["token_auth"] = None
            flask.abort(403)

        pkUser = tokenAuth.get(token_auth)
        return func(pkUser, *args, **kwargs)
    return wrapper


def permissions_required(*permissions:int|Role|str)->object:
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
