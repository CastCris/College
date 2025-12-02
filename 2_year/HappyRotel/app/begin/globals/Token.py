from cryptography.hazmat.primitives.ciphers.aead import AESGCM

import string
import os

## Keys
MASTER_KEY = AESGCM.generate_key(bit_length=256)
SALT_KEY = os.urandom(12)

## Code generate
CODE_PREFIX = ''
CODE_CHARS = string.ascii_letters
CODE_LEN = 16

def code_generate(prefix:str=CODE_PREFIX, chars:str=CODE_CHARS, length:int=CODE_LEN)->str:
    import secrets

    return CODE_PREFIX + (''.join(secrets.choice(chars) for i in range(0, length-len(CODE_PREFIX))))
