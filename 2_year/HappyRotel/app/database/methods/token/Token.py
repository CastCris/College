from database.session import Base

import datetime

##
def id_generate()->str:
    from begin.globals import Crypt

    ID_PREFIX = 'token_'
    ID_LEN = 32

    return Crypt.code_generate(prefix=ID_PREFIX, length=ID_LEN)

def token_generate()->str:
    from begin.globals import Crypt
    import string

    TOKEN_CHARS = string.ascii_letters + string.digits
    TOKEN_LEN = 32

    return Crypt.code_generate(chars=TOKEN_CHARS, length=TOKEN_LEN)

##
class Token(Base):
    __tablename__ = 'Token'

    ##
    DEFAULT_id = id_generate
    DEFAULT_emission_date = datetime.datetime.utcnow

    DEFAULT_token = token_generate

    ##
    def token_wrap(self)->None:
        from database.session import clm_encrypt_phash, model_get, session

        token = model_get(self, "token")[0]
        self.token = clm_encrypt_phash(token)
        session.commit()

    def token_auth(self, token_input:str)->bool:
        from database.session import clm_encrypt_phash_auth, model_get

        token = model_get(self, "token")[0]
        return clm_encrypt_phash_auth(token, token_input)
