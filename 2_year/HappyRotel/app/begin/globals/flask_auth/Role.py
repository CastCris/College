from sqlalchemy import event
from sqlalchemy.orm import Session, DeclarativeMeta, InstrumentedAttribute

##
class Permission():
    def __init__(self, tag:str=None, value:int=None)->None:
        self._TAG: str = tag
        self._VALUE: int = value

    ## Debug pruporse
    """
    def __getattribute__(self, attr_name:str)->'T':
        print(f'{type(self).__name__} call: {attr_name}')
        return super().__getattribute__(attr_name)
    """



    ##
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

    ##
    @tag.setter
    def tag(self, value:str)->None:
        self._TAG = value

    @value.setter
    def value(self, value:int)->None:
        self._VALUE = value

    ##
    def update(self, *args, **kwargs)->None:
        if len(args) == 1 and isinstance(args[0], Permission):
            self.update_from_permission(*args)
        else:
            self.update_from_kwargs(**kwargs)

    def update_from_kwargs(self, **kwargs)->None:
        self._TAG = kwargs.get("tag", self.tag)
        self._VALUE = kwargs.get("value", self.value)

    def update_from_permission(self, permission:"Permission")->None:
        json = permission.json
        for key,value in tuple(json.items()):
            if value is None:
                del json[key]

        self.update_from_kwargs(**json)
    
    ##
    def delete(self)->None:
        self._TAG = None
        self._VALUE = None

    @property
    def deleted(self)->bool:
        return self.tag is None and self.value is None


class PermissionNode():
    def __init__(self, permission:Permission, parent:"PermissionNode"=None)->None:
        self._PERMISSION = permission
        self._PARENT = parent or self
        self._DELETED = False

    ## Debug pruporse
    """
    def __getattribute__(self, attr_name:str)->'T':
        print(f'{type(self).__name__} call: {attr_name}')
        return super().__getattribute__(attr_name)
    """

    ##
    def __getattr__(self, attr_name:str)->'T':
        # print('__getattr__: ', self.permission, attr_name, getattr(self.permission, attr_name, None))
        if hasattr(self.permission, attr_name):
            return getattr(self.permission, attr_name)

        return super().__getattribute__(attr_name)

    ##
    @property
    def permission(self)->Permission:
        return self._PERMISSION

    @property
    def parent(self)->"PermissionNode":
        return self._PARENT

    @property
    def have_parent(self)->bool:
        return not (self.parent is self)


    def update(self, permission:Permission)->None:
        if self.have_parent:
            permission.value = self.parent.value

        self.permission.update(permission)
    
    def delete(self)->None:
        self._DELETED = True
        print('Permission Node delete: ', self.tag, self.have_parent)
        if not self.have_parent:
            self.permission.delete()

    @property
    def deleted(self)->bool:
        return self._DELETED or self.permission.deleted

class PermissionManager():
    def __init__(self, update_func:callable=None)->None:
        self._DICT = {}
        self._UPDATE_ITEM = update_func or (lambda *args, **kwargs:None)

    ## Debug pruporse
    """
    def __getattribute__(self, attr_name:str)->'T':
        print(f'{type(self).__name__} call: {attr_name}')
        return super().__getattribute__(attr_name)
    """

    ##
    def __setitem__(self, key:'T', permission:PermissionNode)->None:
        self.check_class()
        self.p_set(key, permission)

    def __delitem__(self, key:'T')->None:
        self.check_class()
        self.p_del(key)

    def __getitem__(self, key:'T')->PermissionNode:
        self.check_class()
        return self.p_get(key)


    def __repr__(self)->str:
        self.check_class()
        return repr(self.dict)

    def __len__(self)->int:
        self.check_class()
        return len(self.keys())

    ##
    def keys(self)->tuple['T']:
        self.check_class()
        return tuple(self.dict.keys())

    def values(self)->tuple[PermissionNode]:
        self.check_class()
        return self.dict.values()

    def items(self)->tuple[tuple['T', PermissionNode]]:
        self.check_class()
        return self.dict.items()


    def get(self, key:'T', value:'T'=None)->PermissionNode|object:
        if key in self.keys():
            return self[key]
        return value

    def get_raw(self, key:'T', value:'T'=None)->PermissionNode|object:
        if key in self.keys():
            return self.dict[key]
        return value

    ##
    @property
    def dict(self)->dict['T':PermissionNode]:
        return self._DICT


    def p_set(self, key:'T', permission:PermissionNode)->None:
        self.dict[key] = permission

    def p_del(self, key:'T')->None:
        self.dict[key].delete()
        del self.dict[key]

    def p_get(self, key:'T')->PermissionNode:
        permission = self.dict[key]
        return PermissionNode(permission.permission, permission.parent)

    
    def check_key(self, key:str)->None:
        if not key in self.dict.keys():
            return

        permission = self.dict[key]
        if permission.deleted:
            self.p_del(key)
            return

        self._UPDATE_ITEM(self.dict, key, permission)

    def check_class(self)->None:
        for key in list(self.dict.keys()):
            self.check_key(key)

##
class RoleMixin():
    ## Debug pruporse
    """
    def __getattribute__(self, attr_name:str)->'T':
        print(f'{type(self).__name__} call: {attr_name}')
        return super().__getattribute__(attr_name)
    """

    ##
    @staticmethod
    def _tag_permission_update(obj:dict, key:str, permission:PermissionNode)->None:
        if key == permission.tag:
            return

        obj[permission.tag] = permission
        del obj[key]

    @staticmethod
    def _value_permission_update(obj:dict, key:int, permission:PermissionNode)->None:
        if key == permission.value:
            return

        obj[permission.value] = permission
        del obj[key]


    @property
    def tag_permission(self)->dict[str:PermissionNode]:
        if not "_TAG_PERMISSION" in vars(self):
            self._TAG_PERMISSION = PermissionManager(self._tag_permission_update)
        return self._TAG_PERMISSION


    @property
    def value_permission(self)->dict[int:PermissionNode]:
        if not "_VALUE_PERMISSION" in vars(self):
            self._VALUE_PERMISSION = PermissionManager(self._value_permission_update)
        return self._VALUE_PERMISSION

    ##
    @property
    def tags(self)->list[str]:
        return [ tag for tag in self.permissions.keys() ]

    @property
    def tags_value(self)->int:
        return [ value for value in self.permissions.values() ]


    @property
    def permissions(self)->dict[str:int]:
        return {
            permission.tag: permission.value for permission in self.tag_permission.values()
        }

    ##
    def _p_valid(self, permission:PermissionNode)->bool:
        if permission.value in self.value_permission.keys():
            return False
        return True


    ##
    def p_set(self, *permissions:PermissionNode|Permission|dict[str:int], **kwargs)->None:
        if kwargs:
            self._p_set_from_kwargs(**kwargs)
            return
        
        if len(permissions) == 1 and isinstance(permissions[0], dict):
            self._p_set_from_tags(*permissions)
            return

        for p in permissions:
            self._p_set_from_permission(p)


    def _p_set_from_permission(self, permission:Permission|PermissionNode)->None:
        p = permission
        if isinstance(permission , Permission):
            p = PermissionNode(permission)

        if not self._p_valid(p):
                raise AttributeError(f'RoleMixin: Invalid permission {p.tag}')

        self.tag_permission[p.tag] = p
        self.value_permission[p.value] = p

    def _p_set_from_kwargs(self, **kwargs)->None:
        permission = Permission(**kwargs)
        self._p_set_from_permission(permission)

    def _p_set_from_tags(self, tags:dict[str:int])->None:
        for tag, value in tags.items():
            self._p_set_from_kwargs(tag=tag, value=value)


    ##
    def p_get(self, tag:str)->PermissionNode|None:
        return self.tag_permission.get(tag, None)

    def _p_get_raw(self, tag:str)->PermissionNode|None:
        return self.tag_permission.get_raw(tag, None)

    def ps_from_tags(self, *tags:list[str])->int:
        result = 0
        for tag in tags:
            p = self.p_get(tag)
            result += p.value

        return result

    ##
    def p_del(self, *tags:list[str])->None:
        for tag in tags:
            permission = self._p_get_raw(tag)
            permission.delete()


    ##
    def p_upd(self, target:str, permission:Permission|PermissionNode=None, **kwargs)->None:
        if kwargs:
            self._p_upd_from_kwargs(target, **kwargs)
            return

        if permission:
            self._p_upd_from_permission(target, permission)


    def _p_upd_from_permission(self, target:str, permission:Permission|PermissionNode):
        if not self._p_valid(permission):
            return

        p = self._p_get_raw(target)
        if p is None:
            raise AttributeError(f'Invalid permissionn tag: {target}')

        p.update(permission)

    def _p_upd_from_kwargs(self, target:str, **kwargs)->None:
        p = Permission(**kwargs)
        self._p_upd_from_permission(target, p)


    ##
    def p_value_get(self, tag:str)->int|None:
        permission: Permission = self.p_get(tag)
        return permission.value if permission else None

    ##
    def authorized_by_role(self, role:"RoleMixin")->bool:
        return (sum(role.tags_value) & sum(self.tags_value)) == sum(role.tags_value)
    
    def authorized_by_int(self, permission:int)->bool:
        return (permission & sum(self.tags_value)) == permission

    def authorized_by_list_int(self, *permissions)->bool:
        return self.authorized_by_int(sum(permissions))


class Role(RoleMixin):
    def __init__(self, permissions:list[str]|dict[str:int]=None , role:RoleMixin=None)->None:
        if role is None and permissions:
            self._init_from_tags(permissions)
        elif permissions:
            self._init_from_role(role, permissions)

    def _init_from_tags(self, permissions:dict[str:int])->None:
        for tag, value in permissions.items():
            self.p_set(Permission(tag, value))

    def _init_from_role(self, role:RoleMixin, permissions:list[str])->None:
        for tag in permissions:
            permission = role.p_get(tag)
            self.p_set(permission)

##
class Role_ORM(RoleMixin):
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
        self.add(Permission(tag, value))

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
"""
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

print('tags: ',roleEmployer.tags)
print('arole: ', roleEmployer.authorized_by_role(roleAdmin))
print('aint: ', roleEmployer.authorized_by_int(4))

print()
print('tags: ', roleAdmin.tags)
print('aroles: ', roleAdmin.authorized_by_role(roleEmployer))
print('aint: ', roleAdmin.authorized_by_int(1))

roleAdmin.p_upd("MANAGE_INVOICE", Permission('GERENCIAR_FATURA'))
print(roleEmployer.permissions.keys())
"""
