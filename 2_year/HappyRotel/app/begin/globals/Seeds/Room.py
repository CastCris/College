from database.session import *

## Static Instances
class RoomStatus():
    DEPEND_ON = []

    STATUS = {
        'Free': [ 1, True ],
        'Busy': [ 1, False ],
        'Clean': [ 2, True],
        'Dirty': [ 2, False]
    }

    def __init__(self)->None:
        from database.methods import RoomStatus

        ##
        for name, attr in self.STATUS.items():
            value = attr[0]
            positive = attr[1]

            session_insert(RoomStatus, name=name, value=value, positive=positive)

class RoomType():
    DEPEND_ON = []
    # Tag(key): ['description', 10(capacity),  200(price(dollar))]
    TYPES = {
        'High class': [ "Just for who have many money($$$)", 5, 200 ],
        'Middle class': [ "Just for who think are important", 7, 150 ],
        'Lower class': [ "Don't have money but don't want to sleep in street?", 20, 50]
    }

    def __init__(self)->None:
        from database.methods import RoomType

        ##
        for tag, value in self.TYPES.items():
            description = value[0]
            capacity = value[1]
            price = value[2]

            session_insert_SQL(
                RoomType
                , tag=tag
                , description=description
                , capacity=capacity
                , price=price
            )

class RoomLocation():
    DEPEND_ON = []

    # Tag / Tag_prefix / tag_suffix
    TAGS = {
        'Up side': [ 'A', '']
        , 'Terrain': [ '0', '']
        , 'Subsoil': [ '-1', '']
    }

    def __init__(self)->None:
        from database.methods import RoomLocation

        ##
        for tag, value in self.TAGS.items():
            tag_prefix = value[0]
            tag_suffix = value[1]

            session_insert_SQL(
                RoomLocation
                , tag=tag
                , tag_prefix=tag_prefix
                , tag_suffix=tag_suffix
            )

class Room():
    DEPEND_ON = [ 'RoomStatus', 'RoomType' , 'RoomLocation']

    AMOUNT = 10

    def __init__(self)->None:
        from database.methods import Room, RoomType, RoomStatus

        ##
        for i in range(self.AMOUNT):
            type_id = session_SQL(
                """
                SELECT id FROM \"RoomType\"
                ORDER BY RANDOM()
                LIMIT 1
                """
            ).all()[0][0]

            location_id = session_SQL(
                """
                SELECT id FROM \"RoomLocation\"
                ORDER BY RANDOM()
                LIMIT 1
                """
            ).all()[0][0]

            status_value = session_SQL(
                """
                SELECT bit_xor(value)
                FROM (
                    SELECT value FROM \"RoomStatus\"
                    ORDER BY RANDOM()
                    LIMIT (floor(random() * (
                        SELECT COUNT(name) FROM \"RoomStatus\"
                    )) + 1)::int
                ) t;
                """
            ).all()[0][0]

            session_insert(
                Room
                , roomType_id = type_id
                , roomLocation_id = location_id

                , status_value = status_value
           )
