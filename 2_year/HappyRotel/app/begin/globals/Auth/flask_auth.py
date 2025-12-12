from begin.xtensions import flask
from begin.globals import Crypt
import string

##
class Token():
    import string

    ##
    FUNC = Crypt.code_generate()
    CHARS = string.ascii_letters
    LENGTH = 16
    VALIDITY = None

    ##
    def __init__(self, func, chars:str, length:int, validity:int)->None:
        self.FUNC = func
        self.CHARS = chars
        self.length = length
        self.validity = validity

    def generate(*args)->str:
        if not args:
            return Token.FUNC(chars=Token.CHARS, length=Token.LENGTH)

        self = args[0]
        return self.FUNC(chars=self.CHARS, length=self.LENGTH)

tokenAuth = Token(
    Crypt.code_generate,
    string.ascii_letters + string.digits,
    32,
    validity = 60*60*24*7
)

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
            setattr(self, name, value)

        if getattr(self, getattr(self, "permissions_attr_name"), None) is None:
            setattr(self, getattr(self, "permissions_attr_name"), 0)

    def UserAuth(func)->object|None:
        def wrapper():
            self.UserAuth_init()
            return func()

        return wrapper

    ##
    @property
    @UserAuth
    def permissions(self)->int:
        return getattr(self, getattr(self, "permissions_attr_name"))

    @property
    @UserAuth
    def permissions_set(self, value)->int:
        setattr(self, getattr(self, "permissions_attr_name"), value)

    ##
    @UserAuth
    def authorized_by_role(self, role:Role)->bool:
        permissions_role = sum(list(role.tags.values()))
        return (self.permissions & permissions_role) == permissions_role

    @UserAuth
    def authorized_by_tags(self, *tags)->bool:
        for tag in tags:
            if not tag in self.role.tags:
                continue

            permission_tag = self.role.get_tag_value(tag)
            if (self.permissions & permission_tag ) != permission_tag:
                return False

        return True

    @UserAuth
    def authorized_by_int(self, permissions_int:int)->bool:
        return (self.permissions & permissions_int) == permissions_int


    @UserAuth
    def authorized(self, *args)->bool:
        if len(args) == 1 and type(args) == int:
            return self.authorized_by_int(*args)

        if len(args) == 1 and type(args) == Role:
            return self.authorized_by_role(*args)

        return self.authorized_by_tags(*args)

##
def login_required(func)->object:
    def login_required():
        if flask.session.get("user_email", None) is None:
            response = flask.make_response(flask.redirect("/"))
            return response

        return func()
    return login_required

def permission_required(func, permissions:int|Role|list)->object:
    def permission_required():
        from database.session import session_query

        if flask.session.get("user_email", None) is None:
            return 'You don\'t have permission to access this page'

        user_email = flask.session.get("user_email")
        user = session_query(User, 



def login(func)->object:
    def login():
        response = func()
        response_json = response.json

        if not response_json.get("approved", None):
            return response

        flask.session["user_email"] = response_json["user_email"]
        return response
    return login
