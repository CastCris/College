from begin.globals import ManagerUser, Crypt

from sqlalchemy.orm import DeclarativeMeta

import string

##
@ManagerUser.user_get
def user_get(user_id:str)->DeclarativeMeta:
    from database.methods import User
    from database.session import session_query

    return session_query(User, id=user_id)[0]

@ManagerUser.user_unwrap
def user_load(user:DeclarativeMeta)->dict:
    from database.methods import UserInfos
    from database.session import session_query, instance_get, instance_get_columns_value

    ##
    userInfos_id = instance_get(user, "userInfos_id")[0]
    userInfos = session_query(UserInfos, id=userInfos_id)[0]

    user_json = instance_get_columns_value(user)
    userInfos_json = instance_get_columns_value(userInfos)


    return {
        "id":  user_json["id"]
        , "name": userInfos_json["name"]
        , "email": userInfos_json["email"]
    }

## Token configuration
@ManagerUser.tokenKey_gen
def tokenKey_gen()->str:
    return Crypt.code_generate(length=128, chars=string.digits + string.ascii_letters + string.punctuation)

@ManagerUser.token_gen
def token_gen()->str:
    return Crypt.code_generate(length=64, chars=string.digits + string.ascii_letters + string.punctuation)

##
def register_app(app:object)->None:
    pass
