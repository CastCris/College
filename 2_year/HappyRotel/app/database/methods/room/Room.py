from database.session import Base

##
def id_generate()->str:
    from begin.globals import Crypt

    ##
    ID_PREFIX = 'room_'
    ID_LEN = 32

    return Crypt.code_generate(prefix=ID_PREFIX, length=ID_LEN)

##
class Room(Base):
    __tablename__ = 'Room'

    DEFAULT_id = id_generate
    DEFAULT_status_value = 0
