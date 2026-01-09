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

    DOCKER_ADDR = os.getenv("HAPPYROTEL_DOCKER_ADDR", '')

    ## Develop Options
    DEBUG = True

    ## Addictional features(default values)
    ## CookieSession
    COOKIE_TEMPLATE = True
    COOKIE_TEMPLATE_NAME = 'session_deleted.html'

    ## ManagerUser
    MU_TOKEN_TYPE = 'Redis'
    MU_TOKEN_REDIS = redis.Redis.from_url(f"redis://{DOCKER_ADDR}:{REDIS_PORT}", decode_responses=True)

r = redis.Redis(
    host = Config.REDIS_HOST
    , port = int(Config.REDIS_PORT)
    , decode_responses = True
)
r.flushdb()
