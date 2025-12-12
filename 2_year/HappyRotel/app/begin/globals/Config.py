import os
import redis
import itsdangerous
import datetime

##
class Config:
    SECRET_KEY_LEN = 26
    SECRET_KEY = os.urandom(SECRET_KEY_LEN)

    ##
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.Redis(host="localhost", port=2701)

    SESSION_PERMANERT = True
    PERMANET_SESSION_LIFETIME = datetime.timedelta(days=7)

    SESSION_COOKIE_SECURE = True
    SESSION_USE_SIGNER = True

    ##
    DEBUG = True
