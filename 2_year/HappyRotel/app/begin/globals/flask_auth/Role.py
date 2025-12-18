class Permission():
    def __init__(self, tag:str, value:int)->None:
        self.TAG: str = tag
        self.VALUE: int = value

    @property
    def tag(self)->str:
        return self.TAG

    @property
    def value(self)->int:
        return self.VALUE


class Role():
    def __init__(self, tags:dict[str:int] | list[str], **kwargs)->None:
        role = kwargs.get("role", None)

        self.PERMISSIONS:list[Permission] = []

        if not role is None :
            for tag in tags:
                self.PERMISSIONS.append(role.permission_get(tag))
        else:
            for tag_name, tag_value in tags.items():
                self.PERMISSIONS.append(Permission(tag_name, tag_value))
    ##
    @property
    def tags(self)->dict|None:
        return [ permission.tag for permission in self.PERMISSIONS ]

    @property
    def tags_value(self)->int:
        return [ permission.value for permission in self.PERMISSIONS ]

    @property
    def permissions(self)->dict[str:int]:
        return {
            permission.tag: permission.value for permission in self.PERMISSIONS
        }

    def permission_get(self, tag:str)->Permission|None:
        for i in self.PERMISSIONS:
            if i.tag == tag:
                return i

        return None

    def permission_value_get(self, tag:str)->int|None:
        permission: Permission = self.permission_get(tag)
        return permission.value if permission else None


    def authorized_by_role(self, role:"Role")->bool:
        return (sum(role.tags_value) & sum(self.tags_value)) == sum(role.tags_value)
    
    def authorized_by_int(self, permission:int)->bool:
        return (permission & sum(self.tags_value)) == permission

    def authorized_by_tags(self, *tags:list[str])->bool:
        return not False in [ tag in self.tags for tag in tags ]

##
"""
roleAdmin = Role([
    Permission("MANAGE_USER", 1)
    , Permission("MANAGE_ROOM", 2)
    , Permission("MANAGE_INVOICE", 4)
    , Permission("MANAGE_RESERVE", 8)
])

roleEmployer = Role([
    "MANAGE_INVOICE"
    , "MANAGE_RESERVE"
], role=roleAdmin
)

print('tags: ',roleEmployer.tags)
print('arole: ', roleEmployer.authorized_by_role(roleAdmin))
print('aint: ', roleEmployer.authorized_by_int(2))
print('atags: ', roleEmployer.authorized_by_tags("MANAGE_INVOICE", "MANAGE_RESERVE", "MANAGE_USER"))

print()
print('tags: ', roleAdmin.tags)
print('aroles: ', roleAdmin.authorized_by_role(roleEmployer))
print('aint: ', roleAdmin.authorized_by_int(1))
print('atags: ', roleAdmin.authorized_by_tags("MANAGE_INVOICE", "MANAGE_RESERVE", "MANAGE_USER"))
"""
