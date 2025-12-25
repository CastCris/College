from begin.xtensions import redis, datetime, os

##
class Config:
    # Secrety Key
    SECRET_KEY_LEN = 26
    SECRET_KEY = os.urandom(SECRET_KEY_LEN)

    ## Flask Session
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.Redis(host="localhost", port=2701)

    SESSION_PERMANERT = True
    PERMANET_SESSION_LIFETIME = datetime.timedelta(days=7)

    SESSION_COOKIE_SECURE = True
    SESSION_USE_SIGNER = True

    ## Database / Redis
    DB_USER = os.getenv("HAPPYROTEL_DB_USER", '')
    DB_PASSWORD = os.getenv("HAPPYROTEL_DB_PASSWORD", '')
    DB_DATABASE = os.getenv("HAPPYROTEL_DB_DATABASE", '')
    DB_HOST = os.getenv("HAPPYROTEL_DB_HOST", '')

    REDIS_HOST = os.getenv("HAPPYROTEL_REDIS_HOST", '')
    REDIS_PORT = os.getenv("HAPPYROTEL_REDIS_PORT", '')

    ## Develop Options
    DEBUG = True

    ## Addictional features(default values)
    ## CookieSession
    COOKIE_IGNORE = [ 'session' ]
    COOKIE_REQUEST_IGNORE = [ '/static' ]

    COOKIE_SID_NAME = 'sid'
    COOKIE_FLASH_ABLE = True
    COOKIE_FLASH_NAME = 'session_delete'

    ## ManagerUser
    ## pass

r = redis.Redis(
    host = Config.REDIS_HOST
    , port = int(Config.REDIS_PORT)
    , decode_responses = True
)
r.flushdb()
