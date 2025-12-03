from database.session import Base

##
def id_generate()->str:
    from begin.globals import Token

    ##
    ID_PREFIX = 'roomInfos_'
    ID_LEN = 32

    return Token.code_generate(prefix=ID_PREFIX, length=ID_LEN)

##
class RoomInfos(Base):
    __tablename__ = 'RoomInfos'

    DEFAULT_id = id_generate
