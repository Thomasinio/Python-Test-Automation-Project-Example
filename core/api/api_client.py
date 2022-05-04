from furl import furl
from loguru import logger
from pprint import pformat
from requests import Session, Request

from configuration import SERVICE_URL
from .response import Response


def check_for_error(response: Request, *args, **kwargs):
    response.raise_for_status()


def response_logging_hook(response: Request, *args, **kwargs):
    logger.debug(response.url)
    logger.debug(response.status_code)
    logger.debug("\n" + pformat(response.json()))


class ApiClient:

    def __init__(self, base_url=SERVICE_URL):
        self.base_url = furl(base_url)
        self.session = Session()
        # list of functions that are called after every response
        self.session.hooks["response"] = [check_for_error, response_logging_hook]

    def get(self, path="/", params=None):
        url = self.base_url / path
        response = self.session.get(url, params=params)
        return Response(response)

    def post(self, path="/", data=None, json=None):
        url = self.base_url / path
        response = self.session.post(url, data, json)
        return Response(response)
