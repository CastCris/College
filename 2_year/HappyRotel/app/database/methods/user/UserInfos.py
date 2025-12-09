from database.session import Base

##
def id_generate()->str:
    from begin.globals import Crypt

    ##
    ID_PREFIX = 'userInfos_'
    ID_LEN = 32

    return Crypt.code_generate(prefix=ID_PREFIX, length=ID_LEN)

##
class UserInfos(Base):
    __tablename__ = 'UserInfos'

    DEFAULT_id = id_generate
