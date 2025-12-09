from begin.globals import Crypt, Class
from database import *

##
class Seeds():
    SEQUENCE = [
            'TokenType'
            , 'RoomStatus' , 'RoomType' , 'RoomInfos' , 'Room'
            , 'UserPermission', 'UserInfos', 'User'
            , 'Predefined'
            , 'Test'
    ]

    def init()->None:
        import time

        for i in Seeds.SEQUENCE:
            Seeds.__dict__[i].init()

    ## Crypt
    class TokenType():
        import datetime

        # tag / validity(seconds)
        TAGS = {
            "Auth": datetime.timedelta(days=7)
        }

        def init():
            for i in Seeds.TokenType.TAGS.items():
                tag = i[0]
                validity=i[1]

                session_insert_SQL(TokenType, tag=tag, validity=validity)

    ## Rooms
    class RoomStatus():
        STATUS = {
            'Free': [ 1, True ],
            'Busy': [ 1, False ],
            'Clean': [ 2, True],
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

                session_insert_SQL(RoomType, tag=tag, description=description, capacity=capacity, price=price)

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
                session_insert_SQL(RoomInfos, tag=str(locations[location_chosen]), location=location_chosen)

                locations[location_chosen] += 1

    class Room():
        def init()->None:
            from functools import reduce
            from operator import xor

            import random

            ##
            # rooms_infos = [ model_get(i, 'id')[0] for i in session_query(RoomInfos) ]
            # rooms_types = [ model_get(i, 'id')[0] for i in session_query(RoomType) ]
            rooms_infos = [ i[0] for i in session_query(RoomInfos.id) ]
            rooms_types = [ i[0] for i in session_query(RoomType.id) ]
            rooms_status = [ i[0] for i in session_query(RoomStatus.value) ]

            ##
            for i in range(len(rooms_infos)):
                status_selected = [ random.choice(rooms_status) for i in  range(random.randint(1, len(rooms_status)-1)) ]

                info_id = rooms_infos[i]
                type_id = random.choice(rooms_types)
                status_value = reduce(xor, status_selected)


                session_insert_SQL(Room \
                        , roomInfos_id = info_id \
                        , roomType_id = type_id \
                        , status_value = status_value)

    
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
                session_insert_SQL(UserPermission, tag=i[0], value=i[1])

    class UserInfos():
        AMOUNT = 10

        def init()->None:
            from faker import Faker

            ##
            faker = Faker()
            for i in range(Seeds.UserInfos.AMOUNT):
                name = faker.name()
                email = faker.email()

                # session_insert(UserInfos, name=name, email=email)
                session_insert_SQL(UserInfos, name=name, email=email)

    class User():
        def init()->None:
            from begin.globals import Crypt
            import random

            ##
            # userInfos = [ model_get(i, 'id')[0] for i in session_query(UserInfos) ]
            # userPermission = [ model_get(i, 'value')[0] for i in session_query(UserPermission) ]
            userInfos = [ i[0] for i in session_query(UserInfos.id) ]
            userPermission = [ i[0] for i in session_query(UserPermission.value) ]

            for i in userInfos:
                permissions = sum(set([ random.choice(userPermission) for _ in range(random.randint(0, len(userPermission)-1)) ]))
                password_random = Crypt.code_generate()
                # session_insert(User, userInfos_id=i, password=password_random, permissions=permissions)
                session_insert_SQL(User, userInfos_id=i, password=password_random, permissions=permissions)

            """
            query = session_SQL("SELECT u.id, up.tag, up.value FROM \"User\" AS u \
                    LEFT JOIN \"UserPermission\" AS up ON (u.permissions & up.value) = up.value"
            )

            for i in query:
                print(i)
            """

    ##
    class Predefined():
        SEQUENCE = ["UserInfos", "User"]

        PREDEFINED_UserInfos = {
            "id": [
                Crypt.code_generate(prefix="userInfos_", length=32)
            ],

            "name": [
                "Richard"
            ],

            "email": [
                "richard@gmail.com"
            ]
        }

        PREDEFINED_User = {
            "id": [
                Crypt.code_generate(prefix="user_", length=32)
            ],

            "userInfos_id": [
                PREDEFINED_UserInfos["id"][0]
            ],

            "password": [
                "admin"
            ],

            "permissions": [ 
                sum([1, 2, 4, 8])
            ]
        }

        def init()->None:
            for i in Seeds.Predefined.SEQUENCE:
                attr_name = f"PREDEFINED_{i}"
                if not attr_name in Seeds.Predefined.__dict__.keys():
                    continue

                arguments = Seeds.Predefined.__dict__[f"PREDEFINED_{i}"]
                model = model_from_name(i)

                count = len(arguments[list(arguments.keys())[0]])
                for j in range(count):
                    kwargs = { i[0]:i[1][j] for i in arguments.items() }
                    print('predefined kwargs: ', kwargs, model)
                    session_insert_SQL(model, **kwargs)

    ##
    class Test():
        def init()->None:
            import random

            # query_1 = session_query(RoomInfos.id, RoomInfos.hashed_tag, location="Terrain")
            # query_2 = session_query(RoomInfos)

            # print('query_1: ', len(query_1))
            # print('query_2: ', len(query_2))

            admin_permissions = session_SQL("""
            SELECT up.tag, up.value, u.id FROM \"UserPermission\" AS up
            LEFT JOIN \"User\" AS u ON (( u.permissions & up.value) = up.value)
            WHERE u.permissions = 15
            """).all()
            print('admin_permissions: ')
            for i in admin_permissions:
                print(i)

            random_room_id = random.choice(session_query(Room.id))[0]
            random_room_status = session_SQL(f"""
            SELECT r.id, r.status_value, rs.name, rs.value, rs.positive FROM "RoomStatus" AS rs
            LEFT JOIN \"Room\" AS r ON
            (( r.status_value & rs.value ) = rs.value AND rs.positive = TRUE )
            OR
            (( r.status_value & rs.value ) <> rs.value AND rs.positive = FALSE)
            WHERE r.id = '{random_room_id}'
            """).all()

            print(f'Room {random_room_id} status: ')
            for i in random_room_status:
                print(i)


##
def cultivate()->None:
    Seeds.init()
