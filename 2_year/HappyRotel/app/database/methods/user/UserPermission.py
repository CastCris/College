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
