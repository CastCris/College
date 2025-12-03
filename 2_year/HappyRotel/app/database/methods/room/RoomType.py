from database.session import Base

##
def id_generate()->str:
    from begin.globals import Token

    ##
    ID_PREFIX = 'roomType_'
    ID_LEN = 32

    return Token.code_generate(prefix=ID_PREFIX, length=ID_LEN)

##
class RoomType(Base):
    __tablename__ = 'RoomType'

    DEFAULT_id = id_generate
