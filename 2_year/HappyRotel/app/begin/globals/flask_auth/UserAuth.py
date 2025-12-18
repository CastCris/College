from functools import wraps

from .Role import Role

##
class UserAuth():
    ATTRIBUTES = {
        "permissions_attr_name": "permissions",
        "UserAuth_initialized": True
    }

    ##
    def UserAuth_init(self)->None:
        if not getattr(self, "UserAuth_initialized", None) is None:
            return

        for name, value in UserAuth.ATTRIBUTES.items():
            if callable(value):
                setattr(self, name, value())

            setattr(self, name, value)

        if getattr(self, getattr(self, "permissions_attr_name"), None) is None:
            setattr(self, getattr(self, "permissions_attr_name"), 0)

    def UserAuth(func)->object|None:
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            self.UserAuth_init()
            return func(self, *args, **kwargs)

        return wrapper

    ##
    @property
    @UserAuth
    def permissions(self)->int:
        return getattr(self, getattr(self, "permissions_attr_name"))

    @UserAuth
    def permissions_set(self, value)->int:
        setattr(self, getattr(self, "permissions_attr_name"), value)
    
    ##
    @UserAuth
    def authorized_by_role(self, role:Role)->bool:
        return (self.permissions & sum(role.tags_value)) == sum(role.tags_value)

    @UserAuth
    def authorized_by_tags(self, role:Role, *tags)->bool:
        return role.authorized_by_tags(tags)

    @UserAuth
    def authorized_by_int(self, permissions:int)->bool:
        return (self.permissions & permissions) == permissions


    @UserAuth
    def authorized(self, *args)->bool:
        if len(args) == 1 and type(args[0]) == int:
            return self.authorized_by_int(*args)

        if len(args) == 1 and type(args[0]) == Role:
            return self.authorized_by_role(*args)

        return self.authorized_by_tags(*args)
