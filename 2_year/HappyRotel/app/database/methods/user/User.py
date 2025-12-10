from database.session import Base
from begin.globals import flask_auth

##
def id_generate()->str:
    from begin.globals import Crypt

    ##
    ID_PREFIX = 'user_'
    ID_LEN = 32

    return Crypt.code_generate(prefix=ID_PREFIX, length=ID_LEN)

##
RoleAuth = flask_auth.Role({
    'MANAGE_ROOM': 1,
    'MANAGE_USERS': 2,
    'MANAGE_INVOICE': 4,
    'MANAGE_RESERVERS': 8
})

##
class User(Base, flask_auth.UserAuth):
    __tablename__ = 'User'

    DEFAULT_id = id_generate

    ##
    def password_auth(self, password_input:str)->None:
        from database.session.crypt import clm_encrypt_phash_auth
        from database.session import model_get

        ##
        password = model_get(self, "phashed_password")[0]
        return clm_encrypt_phash_auth(password, password_input)
