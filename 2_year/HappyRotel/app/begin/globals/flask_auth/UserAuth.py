from sqlalchemy.orm import DeclarativeMeta

from functools import wraps
from .Role import Role

##
class UserAuth():
    UAUTH_PERMISSION_COLUMN_NAME = "permissions"

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
