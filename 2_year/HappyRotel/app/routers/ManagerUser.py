from begin.globals import ManagerUser

from sqlalchemy.orm import DeclarativeMeta

##
@ManagerUser.user_get
def user_get(user_id:str)->DeclarativeMeta:
    from database.methods import User
    from database.session import session_query

    return session_query(User, id=user_id)

@ManagerUser.user_unwrap
def user_load(user:DeclarativeMeta)->dict:
    from database.session import instance_get_columns_value

    return instance_get_columns_value(user)

def register_app(app:object)->None:
    pass
