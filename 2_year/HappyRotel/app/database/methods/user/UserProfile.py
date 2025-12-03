from database.session import Base

##
def id_generate()->str:
    from begin.globals import Token

    ##
    ID_PREFIX = 'userProfile_'
    ID_LEN = 32

    return Token.code_generate(prefix=ID_PREFIX, length=ID_LEN)

##
class UserProfile(Base):
    __tablename__ = 'UserProfile'

    DEFAULT_id = id_generate
