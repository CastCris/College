from database.session import Base

##
def id_generate()->str:
    from begin.globals import Crypt

    ID_PREFIX = 'roomLocation_'
    ID_LEN = 32

    return Crypt.code_generate(prefix=ID_PREFIX, length=ID_LEN)

##
class RoomLocation(Base):
    __tablename__ = 'RoomLocation'

    DEFAULT_id = id_generate

    def room_tag_generate(self)->str:
        from database.session import session_query
        from database.methods import Room

        ##
        rooms_in_location = len(session_query(Room, roomLocation_id=self.id))
        tag_new = self.tag_prefix + str(rooms_in_location) + self.tag_suffix
        return tag_new
