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

    ##
    def load_json(self)->dict:
        from database.session import instance_get_columns_value

        json = instance_get_columns_value(self)

        return json

    ##
    def room_tag_generate(self)->str:
        from database.session import session_query
        from database.methods import Room

        ##
        rooms_in_location = len(session_query(Room.id, roomLocation_id=self.id))
        tag_new = ''

        for i in range(rooms_in_location):
            tag_new = self.tag_prefix + str(i) + self.tag_suffix
            room = session_query(Room.id, tag=tag_new)
            print('tag_new: ', tag_new)
            if room:
                continue
            return tag_new

        return self.tag_prefix + str(rooms_in_location) + self.tag_suffix

    def room_tag_regenerate(self)->None:
        from database.methods import Room
        from database.session import session_query, instance_get, instance_update

        rooms = session_query(Room, roomLocation_id=instance_get(self, "id")[0])
        for room in rooms:
            instance_update(
                room
                , tag = self.room_tag_generate()
            )
    
    ##
    def update_tag_prefix(self, attr_value)->None:
        self.room_tag_regenerate()

    def update_tag_suffix(self, attr_value)->None:
        self.room_tag_regenerate()
