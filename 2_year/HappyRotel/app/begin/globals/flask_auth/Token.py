from begin.globals import Crypt
import string

##
class Token():
    FUNC = staticmethod(Crypt.code_generate)
    CHARS = string.ascii_letters
    LENGTH = 16
    VALIDITY = None

    CODE = None

    ##
    def __init__(self, func=None, chars:str='', length:int=0, validity:int=None, code:str=None)->None:
        self.FUNC = staticmethod(func) if func else self.FUNC
        self.CHARS = chars or self.CHARS
        self.LENGTH = length or self.LENGTH
        self.VALIDITY = validity or self.VALIDITY

        self.CODE = code or self.CODE


    def generate_code(self)->str:
        token = self.FUNC(length=self.LENGTH, chars=self.CHARS)
        return token

    def generate(self)->str:
        token = self.generate_code()
        return Token(self.FUNC, self.CHARS, self.LENGTH, self.VALIDITY, token)


class TokenAuth():
    FUNC = staticmethod(Crypt.code_generate)
    CHARS = string.ascii_letters + string.digits
    LENGTH = 32
    VALIDITY = 60*60*24*7

    PREFIX = "token:auth"
    KEY_GENERATE = lambda self, token: f"{self.PREFIX}:{token}"

    ##
    def __init__(self, **kwargs)->None:
        super().__init__(**kwargs)

    def generate(self, pk_user:str)->str:
        from begin.globals import r

        ##
        token = self.FUNC(chars=self.CHARS, length=self.LENGTH)
        key = self.KEY_GENERATE(token)
        r.hset(key, mapping=pk_user)
        r.expire(key, self.VALIDITY)

        return token

    def remove(self, token:str)->None:
        from begin.globals import r

        ##
        r.delete(self.KEY_GENERATE(token))

    def auth(self, token:str)->bool:
        from begin.globals.Config import r

        return True if r.hgetall(f"{self.PREFIX}:{token}") else False

    def get(self, token:str)->str:
        from begin.globals.Config import r

        return r.hgetall(self.KEY_GENERATE(token))

tokenAuth = TokenAuth()
