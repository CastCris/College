from begin.globals import UserAuth
from database.session import Base

##
def id_generate()->str:
    from begin.globals import Crypt

    ##
    ID_PREFIX = 'user_'
    ID_LEN = 32

    return Crypt.code_generate(prefix=ID_PREFIX, length=ID_LEN)

##
# print(UserAuth.UAUTH_PERMISSION_COLUMN_NAME)
# class User(Base, UserAuth):
class User(Base, UserAuth):
    __tablename__ = 'User'

    DEFAULT_id = id_generate

    ##
    @property
    def permissions_json(self)->dict[str:str]:
        from database.methods import UserPermission
        from database.session import session_SQL, instance_get

        user_id = instance_get(self, "id")[0]
        userPermissions = session_SQL(f"""
        SELECT up.id, up.tag FROM \"User\" AS u
        LEFT JOIN \"UserPermission\" AS up
        ON
            ( u.permissions & up.value ) = up.value AND 
            (( up.value = 0 AND u.permissions = 0) OR ( up.value <> 0 AND u.permissions <> 0 ))
        WHERE u.id = '{user_id}'
        """).all()

        return { row[0]:row[1] for row in userPermissions }

    def load_json(self)->dict:
        from database.methods import UserInfos
        from database.session import session_query, instance_get, instance_get_columns_value

        ##
        user_id = instance_get(self, "id")[0]

        userInfos_id = instance_get(self, "userInfos_id")[0]
        userInfos = session_query(UserInfos, id=userInfos_id)[0]

        user_name, user_email = instance_get(userInfos, "name", "email")
        user_permissionsJson = self.permissions_json

        ##
        return {
            "id": user_id

            , "userInfos_id": userInfos_id
            , "name": user_name
            , "email": user_email

            , "permissions": user_permissionsJson
        }

    ##
    def password_auth(self, password_input:str)->None:
        from database.session.crypt import clm_encrypt_phash_auth
        from database.session import instance_get

        ##
        password = instance_get(self, "phashed_password")[0]
        return clm_encrypt_phash_auth(password, password_input)

