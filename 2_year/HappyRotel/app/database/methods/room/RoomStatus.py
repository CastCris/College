from database.session import Base

##
def id_generate()->None:
    from begin.globals import Crypt

    ID_PREFIX = 'roomStatus_'
    ID_LEN = 16

    return Crypt.code_generate(prefix=ID_PREFIX, length=ID_LEN)

##
class RoomStatus(Base):
    __tablename__ = 'RoomStatus'

    DEFAULT_id = id_generate

    ##
    def load_json(self)->dict:
        from database.session import instance_get_columns_value

        json = instance_get_columns_value(self)
        return json
