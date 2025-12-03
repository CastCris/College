from begin.globals import Token, Class
from database import *

##
class Seeds():
    SEQUENCE = [
        'RoomStatus' , 'RoomType' , 'RoomInfos' , 'Room', 'RoomStatusItem' \
        , 'UserPermission', 'UserInfos', 'User'
    ]

    ##
    def init()->None:
        for i in Seeds.SEQUENCE:
            Seeds.__dict__[i].init()


    ## Rooms
    class RoomStatus():
        STATUS = {
            'Free': [ 1, True ],
            'Busy': [ 1, False ],
            'Clan': [ 2, True],
            'Dirty': [ 2, False]
        }

        def init()->None:
            for i in Seeds.RoomStatus.STATUS.items():
                value = i[1][0]
                positive = i[1][1]

                session_insert(RoomStatus, name=i[0], value=value, positive=positive)

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
            rooms_infos = [ model_get(i, 'id')[0] for i in session_query(RoomInfos) ]
            rooms_types = [ model_get(i, 'id')[0] for i in session_query(RoomType) ]

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
            rooms_status = [ model_get(i, 'value')[0] for i in session_query(RoomStatus) ]

            for i in rooms:
                status = [ random.choice(rooms_status) for i in range(random.randint(0, len(rooms_status)-1)) ]
                status_value = 0
                for j in status:
                    status_value ^= j

                model_update(i, status_value=status_value)

    
    ## User
    class UserPermission():
        TAGS = {
            'MANAGE_ROOM': 1,
            'MANAGE_USERS': 2,
            'MANAGE_INVOICE': 4,
            'MANAGE_RESERVERS': 8
        }

        def init()->None:
            for i in Seeds.UserPermission.TAGS.items():
                session_insert(UserPermission, tag=i[0], value=i[1])

    class UserInfos():
        AMOUNT = 50

        def init()->None:
            from faker import Faker

            ##
            faker = Faker()
            for i in range(Seeds.UserInfos.AMOUNT):
                name = faker.name()
                email = faker.email()

                session_insert(UserInfos, name=name, email=email)

    class User():
        def init()->None:
            from begin.globals import Token
            import random

            ##
            userInfos = [ model_get(i, 'id')[0] for i in session_query(UserInfos) ]
            userPermission = [ model_get(i, 'value')[0] for i in session_query(UserPermission) ]

            for i in userInfos:
                permissions = sum(set([ random.choice(userPermission) for _ in range(random.randint(0, len(userPermission)-1)) ]))
                password_random = Token.code_generate()

                session_insert(User, userInfos_id=i, password=password_random, permissions=permissions)

def cultivate()->None:
    Seeds.init()
