from database.session import *

##
class PredefinedUser():
    DEPEND_ON = []

    NAMES = [
        "Richard"
        , "Abreu"
        , "GenericEmployer"
    ]

    EMAILS = [
        "richard@gmail.com"
        , "abreu@gmail.com"
        , "genericEmployer@gmail.com"
    ]

    PERMISSIONS = [
        15
        , 0
        , 12
    ]

    PASSWORDS = [
        'admin'
        , 'admin'
        , 'admin'
    ]

    def __init__(self)->None:
        from database.methods import User, UserInfos

        for i in range(len(self.NAMES)):
            # userInfos
            name = self.NAMES[i]
            email = self.EMAILS[i]

            #user
            permissions = self.PERMISSIONS[i]
            password = self.PASSWORDS[i]
            
            userInfos = session_insert(UserInfos, name=name, email=email)
            user = session_insert(
                User
                , userInfos_id=instance_get(userInfos, "id")[0]
                , permissions=permissions
                , password = password
            )

class Predefined():
    DEPEND_ON = ['PredefinedUser']

    def __init__(self)->None:
        pass
