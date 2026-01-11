from sqlalchemy import event
from sqlalchemy.orm import Session, DeclarativeMeta, InstrumentedAttribute

##
class Permission():
    def __init__(self, tag:str, value:int)->None:
        self._TAG: str = tag
        self._VALUE: int = value

    @property
    def tag(self)->str:
        return self._TAG

    @property
    def value(self)->int:
        return self._VALUE

    @property
    def json(self)->dict[str:int]:
        return {
            "tag": self.tag
            , "value": self.value
        }


    def update(self, *args, **kwargs)->None:
        if len(args) == 1 and isinstance(args[0], Permission):
            self.update_from_permission(*args)
        else:
            self.update_from_kwargs(**kwargs)

    def update_from_kwargs(self, **kwargs)->None:
        self._TAG = kwargs.get("tag", self.tag)
        self._VALUE = kwargs.get("value", self.value)

    def update_from_permission(self, permission:"Permission")->None:
        self.update_from_kwargs(**permission.json)
    

    def delete(self)->None:
        self._TAG = None
        self._VALUE = None

    @property
    def deleted(self)->bool:
        return self.tag is None and self.value is None

##
class RolePermissionManager():
    def __init__(self)->None:
        self._DICT = {}


    def __getitem__(self, key:'T')->Permission:
        self.permission_check(key)
        return self.dict[key]

    def __setitem__(self, key:'T', permission:Permission)->None:
        self.dict[key] = permission

    def __delitem__(self, key:'T')->None:
        del self.dict[key]

    def __repr__(self)->str:
        for key in self.keys():
            self.permission_check(key)
        return repr(self.dict)

    def __len__(self)->int:
        return len(self.keys())


    def keys(self)->tuple:
        return tuple(self.dict.keys())

    def items(self)->list[tuple]:
        return self.dict.items()

    def values(self)->tuple:
        return tuple(self.dict.values())


    def get(self, key:'T', *args)->Permission:
        self.permission_check(key)
        return self.dict.get(key, *args)

    ##
    @property
    def dict(self)->dict['T':Permission]:
        return self._DICT
    
    def permission_check(self, key:'T')->None:
        if self.dict[key].deleted:
            del self.dict[key]

class RoleMixin():
    @property
    def tag_permission(self)->dict[str:Permission]:
        if not "_TAG_PERMISSION" in vars(self):
            self._TAG_PERMISSION = RolePermissionManager()

        return self._TAG_PERMISSION

    @tag_permission.setter
    def tag_permission(self, permissions:list[Permission])->None:
        self._TAG_PERMISSION = RolePermissionManager()
        for permission in permissions:
            self._TAG_PERMISSION[permission.tag] = permission


    @property
    def value_permission(self)->dict[int:Permission]:
        if not "_VALUE_PERMISSION" in vars(self):
            self._VALUE_PERMISSION = RolePermissionManager()

        return self._VALUE_PERMISSION

    @value_permission.setter
    def value_permission(self, permissions:list[Permission])->None:
        self._VALUE_PERMISSION = RolePermissionManager()
        for  permission in permissions:
            self._VALUE_PERMISSION[permission.value] = permission


    ##
    @property
    def tags(self)->dict|None:
       return [ tag for tag in self.permissions.keys() ]

    @property
    def tags_value(self)->int:
        return [ value for value in self.permissions.values() ]


    @property
    def permissions(self)->dict[str:int]:
        return {
            permission.tag: permission.value for permission in self.tag_permission.values()
        }

    def permissions_from_tags(self, *tags)->int:
        return sum([ value for tag, value in self.permissions if tag in tags])

    def permission_valid(self, permission:Permission)->bool:
        if permission.value in self.value_permission:
            return False
        return 

    ##
    def permission_add(self, permission:Permission)->None:
        if permission.value in self.value_permission.keys():
            return

        self.tag_permission[permission.tag] = permission
        self.value_permission[permission.value] = permission

    def permission_del(self, permission:Permission)->None:
        del self.tag_permission[permission.tag]
        del self.value_permission[permission.value]

    def permission_get(self, tag:str)->Permission|None:
        return self.tag_permission.get(tag, None)

    def permission_swap(self, tag:str, permission_swap:Permission)->None:
        permission = self.permission_get(tag)
        self.permission_del(permission)

        permission.update(permission_swap)
        self._TAG_PERMISSION[permission.tag] = permission

    def permission_value_get(self, tag:str)->int|None:
        permission: Permission = self.permission_get(tag)
        return permission.value if permission else None

    ##
    def authorized_by_role(self, role:"RoleMixin")->bool:
        return (sum(role.tags_value) & sum(self.tags_value)) == sum(role.tags_value)
    
    def authorized_by_int(self, permission:int)->bool:
        return (permission & sum(self.tags_value)) == permission


class Role(RoleMixin):
    def __init__(self, permissions:list[str] | dict[str:int] , role:RoleMixin=None)->None:
        if role is None:
            self.init_from_tags(permissions)
        else:
            self.init_from_role(role, permissions)

    def init_from_tags(self, permissions:dict[str:int])->None:
        for tag, value in permissions.items():
            self.permission_add(Permission(tag, value))

    def init_from_role(self, role:RoleMixin, permissions:list[str])->None:
        for tag in permissions:
            permission = role.permission_get(tag)
            self.permission_add(permission)

##
class Role_ORM():
    _TABLE_COLUMN_TAG_NAME = 'tag'
    _TABLE_COLUMN_VALUE_NAME = 'value'

    def __init__(self, table:DeclarativeMeta, **kwargs)->None:
        self._TABLE = table
        self._TABLE_COLUMN_TAG_NAME = kwargs.get("column_tag_name") or self._TABLE_COLUMN_TAG_NAME
        self._TABLE_COLUMN_VALUE_NAME = kwargs.get("column_value_name") or self._TABLE_COLUMN_VALUE_NAME

        if None in [ self.column_tag, self.column_value ]:
            raise AttributeError(f"Plase, ensure that the columns {self.column_tag_name} and {self.column_value_name} exists in table {self.table.__tablename}")

        ##
        for table_i in self.session.query(self.table):
            self.permission_add_from_orm(table_i)

        event.listen(self.table, "after_insert", self.permission_insert)
        event.listen(self.table, "before_delete", self.permission_delete)
        
    ##
    def permission_add_from_orm(self, table_i:DeclarativeMeta)->None:
        tag, value = getattr(table_i, self.column_tag_name, None), getattr(table_i, self.column_value_name, None)
        self.permission_add(Permission(tag, value))

    def permission_del_from_orm(self, table_i:DeclarativeMeta)->None:
        tag = getattr(table_id, self.column_tag_name, None)
        self.permission_del(tag)
    
    ##
    def permission_insert(self, mapper, connection, instance)->None:
        self.permission_add_from_orm(instance)

    def permission_delete(self, mapper, connection, instance)->None:
        self.permission_del_from_orm(instance)

    ##
    @property
    def table(self)->DeclarativeMeta:
        return self._TABLE

    
    @property
    def column_tag_name(self)->str:
        return self._TABLE_COLUMN_TAG_NAME

    @property
    def column_value_name(self)->str:
        return self._TABLE_COLUMN_VALUE_NAME


    @property
    def column_tag(self)->InstrumentedAttribute|None:
        return getattr(self.table, self.column_tag_name, None)

    @property
    def column_value(self)->InstrumentedAttribute|None:
        return getattr(self.table, self.column_value_name, None)


    @property
    def session(self)->Session:
        return self._SESSION

##
roleAdmin = Role({
    "MANAGE_USER": 1
    , "MANAGE_ROOM": 2
    , "MANAGE_INVOICE": 4
    , "MANAGE_RESERVE": 8
})

roleEmployer = Role([
    "MANAGE_INVOICE"
    , "MANAGE_RESERVE"
], role=roleAdmin
)

"""
print('tags: ',roleEmployer.tags)
print('arole: ', roleEmployer.authorized_by_role(roleAdmin))
print('aint: ', roleEmployer.authorized_by_int(11))

print()
print('tags: ', roleAdmin.tags)
print('aroles: ', roleAdmin.authorized_by_role(roleEmployer))
print('aint: ', roleAdmin.authorized_by_int(1))
"""
roleAdmin.permission_swap("MANAGE_INVOICE", Permission('GERENCIAR_FATURA', 1))
print(roleEmployer.permissions.keys())
