from database.session import *

##
def id_generate()->str:
    from begin.globals import Crypt

    ##
    ID_PREFIX = 'roomInfos_'
    ID_LEN = 32

    return Crypt.code_generate(prefix=ID_PREFIX, length=ID_LEN)

##
class RoomInfos(Base):
    __tablename__ = 'RoomInfos'

    DEFAULT_id = id_generate
