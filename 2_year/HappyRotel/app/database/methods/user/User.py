from database.session import Base

##
def id_generate()->str:
    from begin.globals import Token

    ##
    ID_PREFIX = 'user_'
    ID_LEN = 32

    return Token.code_generate(prefix=ID_PREFIX, length=ID_LEN)

##
class User(Base):
    __tablename__ = 'User'

    DEFAULT_id = id_generate

    ##
    def password_auth(password_input:str)->None:
        from database.session.crypt import clm_encrypt_phash_auth
        from database.session import model_get

        ##
        password = model_get("phashed_password")

        return clm_encrypt_phash_auth(password, password_input)
