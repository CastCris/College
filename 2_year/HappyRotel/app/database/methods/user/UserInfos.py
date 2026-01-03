from database.session import Base

##
def id_generate()->str:
    from begin.globals import Crypt

    ##
    ID_PREFIX = 'userInfos_'
    ID_LEN = 32

    return Crypt.code_generate(prefix=ID_PREFIX, length=ID_LEN)

##
class UserInfos(Base):
    __tablename__ = 'UserInfos'

    DEFAULT_id = id_generate

    ##
    def load_json(self)->dict:
        from database.methods import User
        from database.session import session_query, instance_get_columns_value

        json = instance_get_columns_value(self)
        user_id = session_query(User.id, userInfos_id=json["id"])[0][0]

        return {
            "id": json["id"]
            , "user_id": user_id
            , "name": json["name"]
            , "email": json["email"]
        }
