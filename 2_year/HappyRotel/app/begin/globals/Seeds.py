from begin.globals import Token, Class
from database import *

##
class Seeds():
    SEQUENCE = ['RoomStatus' , 'RoomType' , 'RoomInfos' ] #, 'Room', 'RoomStatusItem']

    ##
    def init()->None:
        for i in Seeds.SEQUENCE:
            Seeds.__dict__[i].init()

    class RoomStatus():
        STATUS = {
            'Free': 1,
            'Busy': 2,
            'Dirty': 4
        }

        def init()->None:
            for i in Seeds.RoomStatus.STATUS.items():
                session_insert(RoomStatus, name=i[0], value=i[1])

    class RoomType():
        # Tag(key): ['description', 10(capacity),  200(price(dollar))]
        TYPES = {
            'High class': [ "Just for who have many money($$$)", 5, 200 ],
            'Middle class': [ "Just for who think are important", 7, 150 ],
            'Lower class': [ "Don't have money but don't want to sleep in street?", 20, 50]
        }

        def init()->None:
            for i in Seeds.RoomType.TYPES.items():
                description = i[1][0]
                capacity = i[1][1]
                price = i[1][2]
                tag = i[0]

                session_insert(RoomType, tag=tag, description=description, capacity=capacity, price=price)

    class RoomInfos():
        AMOUNT = 10
        LOCATIONS = {
            'Up side': 100,
            'Terrain': 0,
            'Subsoil': -100
        }

        def init()->None:
            import random

            ##
            locations = Seeds.RoomInfos.LOCATIONS

            for i in range(Seeds.RoomInfos.AMOUNT):
                location_chosen = random.choice(list(locations.keys()))
                session_insert(RoomInfos, tag=str(locations[location_chosen]), location=location_chosen)

                locations[location_chosen] += 1

    class Room():
        def init()->None:
            import random

            ##
            rooms_infos = [ model_get('id', i)[0] for i in session_query(RoomInfos) ]
            rooms_types = [ model_get('id', i)[0] for i in session_query(RoomType) ]

            ##
            for i in range(len(rooms_infos)):
                info_id = rooms_infos[i]
                type_id = random.choice(rooms_types)

                session_insert(Room \
                        , roomInfos_id = info_id \
                        , roomType_id = type_id)
    
    class RoomStatusItem():
        def init()->None:
            import random

            ##
            rooms = session_query(Room)
            rooms_status = [ model_get('id', i)[0] for i in session_query(RoomStatus) ]

            for i in rooms:
                status = [ random.choice(rooms_status) for i in range(random.randint(0, len(rooms_status)-1)) ]

                for j in status:
                    session_insert(RoomStatusItem \
                            , roomStatus_id = j \
                            , room_id = i)

def cultivate()->None:
    Seeds.init()
