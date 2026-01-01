from database.session import Base

##
def id_generate()->str:
    from begin.globals import Crypt

    ##
    ID_PREFIX = 'roomType_'
    ID_LEN = 32

    return Crypt.code_generate(prefix=ID_PREFIX, length=ID_LEN)

##
class RoomType(Base):
    __tablename__ = 'RoomType'

    DEFAULT_id = id_generate

    ##
    def load_json(self)->None:
        from database.session import instance_get_columns_value

        json = instance_get_columns_value(self)
        return {
            'id': json['id']
            , 'tag': json['tag']
            , 'description': json['description']

            , 'capacity': json['capacity']
            , 'price': json['price']
        }
