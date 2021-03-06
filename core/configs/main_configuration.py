from environs import Env
from furl import furl

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
