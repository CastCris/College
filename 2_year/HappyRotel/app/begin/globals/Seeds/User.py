from database.session import *

class UserPermission():
    DEPEND_ON = []

    def __init__(self)->None:
        from begin.globals import roleAdmin
        from database.methods import UserPermission

        for tag, value in roleAdmin.permissions.items():
            session_insert_SQL(UserPermission, tag=tag, value=value)

class UserInfos():
    DEPEND_ON = ['UserPermission']
    AMOUNT = 10

    def __init__(self)->None:
        from database.methods import UserInfos
        from faker import Faker

        ##
        faker = Faker()
        for i in range(self.AMOUNT):
            name = faker.name()
            email = faker.email()

            # session_insert(UserInfos, name=name, email=email)
            session_insert_SQL(UserInfos, name=name, email=email)

class User():
    DEPEND_ON = [ 'UserInfos', 'UserPermission' ]

    def __init__(self)->None:
        from begin.globals import Crypt
        from database.methods import User, UserInfos, UserPermission
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

        """
        query = session_SQL("SELECT u.id, up.tag, up.value FROM \"User\" AS u \
                LEFT JOIN \"UserPermission\" AS up ON (u.permissions & up.value) = up.value"
        )

        for i in query:
            print(i)
