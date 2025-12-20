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

    ##
    def __init__(self, **kwargs)->None:
        super().__init__(**kwargs)
        print('ABCD')
        self.tag_generate()

    def tag_generate(self)->str:
        from database.session import session_query, model_get, model_update
        from database.methods import RoomLocation

        ##
        roomLocation_id = model_get(self, "roomLocation_id")[0]
        roomLocation = session_query(RoomLocation, id=roomLocation_id)[0]

        model_update(
            self
            , tag=roomLocation.room_tag_generate()
        )

    def load_json(self)->dict:
        from database.session import session_query, session_SQL, model_get_columns_value
        from database.methods import RoomType, RoomLocation

        ##
        room  = model_get_columns_value(self)

        room_type = model_get_columns_value(
            session_query(RoomType, id=room["roomType_id"])[0]
        )

        room_location = model_get_columns_value(
            session_query(RoomLocation, id=room["roomLocation_id"])[0]
        )

        room_status = session_SQL(f"""
        SELECT rs.name FROM \"Room\" as r
        LEFT JOIN \"RoomStatus\" AS rs ON 
            (
            (( r.status_value & rs.value ) = rs.value AND rs.positive = TRUE)
            OR
            (( r.status_value & rs.value ) <> rs.value AND rs.positive = FALSE)
            )
        WHERE r.id = '{room["id"]}'
        """).all()[0][0]
        # print('room_infos: ', room_infos)

        return {
            'tag': room["tag"],

            'type': room_type["tag"],
            'price': room_type['price'],
            'capacity': room_type["capacity"],
            'description': room_type["description"],

            'location': room_location["tag"],

            'status': room_status
        }
    
