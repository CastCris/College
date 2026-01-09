from cryptography.hazmat.primitives.ciphers.aead import AESGCM

import string
import os

## Keys
MASTER_KEY = AESGCM.generate_key(bit_length=256)

SHA256_SALT_KEY_DB = os.urandom(12)
SHA256_SALT_KEY = os.urandom(12)

## Code generate
CODE_PREFIX = ''
CODE_CHARS = string.ascii_letters
CODE_LEN = 16

def code_generate(prefix:str=CODE_PREFIX, chars:str=CODE_CHARS, length:int=CODE_LEN)->str:
    import secrets

    return prefix + (''.join(secrets.choice(chars) for i in range(0, length-len(prefix))))

## Argon implementation
def argon2_crypt(text:str, **kwargs)->str:
    from argon2 import PasswordHasher

    hasher = PasswordHasher(**kwargs)
    return hasher.hash(text)

def argon2_auth(text_hashed:str, text:str)->bool:
    from argon2 import PasswordHasher

    hasher = PasswordHasher()
    try:
        return hasher.verify(text_hashed, text)

    except:
        return False

## Sha256 Implementation
def sha256_crypt(value:str, salt:bytes=SHA256_SALT_KEY)->str:
    import hashlib
    import base64

    hashed_value = hashlib.sha256(value.encode() + salt).digest()
    return base64.b64encode(hashed_value).decode()
