from furl import furl
from environs import Env

from src.utils import make_namedtuple


env = Env()
env.read_env()  # Read .env into os.environ


# Register a new parser method for paths
@env.parser_for("furl")
def furl_parser(value):
    return furl(value)


SERVICE_HOST = env.furl("SERVICE_HOST")
AUTH0_HOST = env.furl("AUTH0_HOST")
AUTH0_CLIENT_ID = env("AUTH0_CLIENT_ID")
AUTH0_CLIENT_SECRET = env("AUTH0_CLIENT_SECRET")
AUTH0_GRANT_TYPE = env("AUTH0_GRANT_TYPE")
"""
Set the timeout thresholds for the maximum amount of time in seconds that requests should wait before stopping. 
The first element, `connection_timeout`, represents the maximum time allowed for establishing a connection to the server. 
The second element, `data_read_timeout`, represents the maximum time allowed for receiving a response from the server, 
once a connection has been established.
"""
TIMEOUT_THRESHOLD = make_namedtuple("TimeoutThreshold", connection_timeout=0.5, data_read_timeout=5)
