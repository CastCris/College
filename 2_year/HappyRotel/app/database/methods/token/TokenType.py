from database.session import Base

##
def id_generate():
    from begin.globals import Crypt

    ##
    ID_PREFIX = 'tokenType_'
    ID_LEN = 32

    return Crypt.code_generate(prefix=ID_PREFIX, length=ID_LEN)

##
class TokenType(Base):
    __tablename__ = 'TokenType'
    DEFAULT_id = id_generate
