from database.session import Base

##
def id_generate()->str:
    from begin.globals import Crypt

    ##
    ID_PREFIX = 'userProfile_'
    ID_LEN = 32

    return Crypt.code_generate(prefix=ID_PREFIX, length=ID_LEN)

##
class UserPermission(Base):
    __tablename__ = 'UserPermission'

    DEFAULT_id = id_generate

    ##
    def load_json(self)->dict:
        from database.session import instance_get_columns_value

        json = instance_get_columns_value(self)
        return json

