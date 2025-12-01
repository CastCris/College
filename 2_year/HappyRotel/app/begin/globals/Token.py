from cryptography.hazmat.primitives.ciphers.aead import AESGCM

MASTER_KEY = AESGCM.generate_key(bit_length=256)
