from furl import furl
from environs import Env

from src.utils import make_namedtuple


env = Env()
# Read .env into os.environ
env.read_env()


# Register a new parser method for paths
@env.parser_for("furl")
def furl_parser(value):
    return furl(value)


SERVICE_HOST = env.furl("SERVICE_HOST")  # -> furl object
AUTH0_HOST = env.furl("AUTH0_HOST")

AUTH0_CLIENT_ID = env("AUTH0_CLIENT_ID")
AUTH0_CLIENT_SECRET = env("AUTH0_CLIENT_SECRET")
AUTH0_GRANT_TYPE = env("AUTH0_GRANT_TYPE")

"""
Set timeout to the amount of time in seconds requests should wait until stopping.
The first element represent the amount of time allowed for connecting to the server,
and the second represent the amount of time to wait on a response once a connection has been established.
"""
TIMEOUT_THRESHOLD = make_namedtuple("TimeoutThreshold", connection_timeout=5, data_read_timeout=10)
