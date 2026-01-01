from database.session import Base
from sqlalchemy.orm import DeclarativeMeta

##
def id_generate()->str:
    from begin.globals import Crypt

    ##
    ID_PREFIX = 'room_'
    ID_LEN = 32

    return Crypt.code_generate(prefix=ID_PREFIX, length=ID_LEN)

def tag_generate(roomLocation_id:str)->str:
    from database.session import session_query, instance_get
    from database.methods import RoomLocation

    ##
    roomLocation = session_query(RoomLocation, id=roomLocation_id)[0]
    return roomLocation.room_tag_generate()


##
class Room(Base):
    __tablename__ = 'Room'

    DEFAULT_id = id_generate
    DEFAULT_status_value = 0

    ##
    SQL_GET_STATUS = lambda self, room_id: f"""
    SELECT rs.tag FROM \"Room\" as r
    LEFT JOIN \"RoomStatus\" AS rs ON
    (( rs.value & r.status_value ) = rs.value AND rs.positive )
    OR
    (( rs.value & r.status_value ) <> rs.value AND NOT rs.positive )
    WHERE r.id = '{room_id}'
    """

    ##
    def create_roomLocation_id(self, attr_value)->None:
        from database.session import instance_update

        tag = tag_generate(attr_value)
        instance_update(self, tag=tag)

    ##
    def update_roomLocation_id(self, attr_value)->None:
        from database.session import instance_update, instance_get

        tag = tag_generate(attr_value)
        instance_update(self, tag=tag)

    ##
    def load_json(self)->dict:
        from database.session import session_query, session_SQL, instance_get_columns_value
        from database.methods import RoomType, RoomLocation

        ##
        room  = instance_get_columns_value(self)
        print('room_json: ', room)

        room_type = instance_get_columns_value(
            session_query(RoomType, id=room["roomType_id"])[0]
        )

        room_location = instance_get_columns_value(
            session_query(RoomLocation, id=room["roomLocation_id"])[0]
        )

        room_status = self.get_status()
        print('room_status: ', room_status)

        return {
            'id': room['id']
            , 'tag': room["tag"]

            , 'type': room_type["tag"]
            , 'price': room_type['price']
            , 'capacity': room_type["capacity"]
            , 'description': room_type["description"]

            , 'location': room_location["tag"]

            , 'status': room_status
        }

    def get_status(self)->tuple:
        from database.session import session_SQL, instance_get

        room_status = [ tag[0] for tag in session_SQL(self.SQL_GET_STATUS(instance_get(self, "id")[0])).all() ]
        return room_status
