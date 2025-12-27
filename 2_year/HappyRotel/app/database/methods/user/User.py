from begin.globals import UserAuth
from database.session import Base

##
def id_generate()->str:
    from begin.globals import Crypt

    ##
    ID_PREFIX = 'user_'
    ID_LEN = 32

    return Crypt.code_generate(prefix=ID_PREFIX, length=ID_LEN)

##
# print(UserAuth.UAUTH_PERMISSION_COLUMN_NAME)
# class User(Base, UserAuth):
class User(Base, UserAuth):
    __tablename__ = 'User'

    DEFAULT_id = id_generate

    ##
    def password_auth(self, password_input:str)->None:
        from database.session.crypt import clm_encrypt_phash_auth
        from database.session import instance_get

        ##
        password = instance_get(self, "phashed_password")[0]
        return clm_encrypt_phash_auth(password, password_input)
