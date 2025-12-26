from functools import wraps
from sqlalchemy import event
from sqlalchemy.orm import DeclarativeMeta

from database.methods import User

from .Role import Role

##
class UserAuth():
    UAUTH_PERMISSION_COLUMN_NAME = "permission"

    ##
    def __init_subclass__(cls, **kwargs)->None:
        from database.session import model_get_columns_name

        if getattr(cls, "UAUTH_INITIALIZED", None):
            return

        print('userAuth: ', isinstance(cls, DeclarativeMeta), vars(cls))
        if not cls.UAUTH_PERMISSION_COLUMN_NAME in model_get_columns_name(cls):
            raise AttributeError(f'UserAuth: The table {cls.__name__} require the {cls.UAUTH_PERMISSION_COLUMN_NAME} column. Put this column before continue')

        setattr(cls, cls.UAUTH_INITIALIZED, True)

    def UserAuth(func)->object|None:
        @wraps(func)
        def wrapper(*args, **kwargs):
            UserAuth.UserAuth_init()
            return func(*args, **kwargs)

        return wrapper

    ##
    @property
    def permissions(self)->int:
        return getattr(self, getattr(self, self.UAUTH_PERMISSION_COLUMN_NAME))

    @permissions.setter
    def permissions(self, value)->int:
        setattr(self, getattr(self, self.UAUTH_PERMISSION_COLUMN_NAME), value)
    
    ##
    def authorized_by_role(self, role:Role)->bool:
        return (self.permissions & sum(role.tags_value)) == sum(role.tags_value)

    def authorized_by_tags(self, role:Role, *tags)->bool:
        return role.authorized_by_tags(tags)

    def authorized_by_int(self, permissions:int)->bool:
        return (self.permissions & permissions) == permissions


    def authorized(self, *args)->bool:
        if len(args) == 1 and type(args[0]) == int:
            return self.authorized_by_int(*args)

        if len(args) == 1 and type(args[0]) == Role:
            return self.authorized_by_role(*args)

        return self.authorized_by_tags(*args)
