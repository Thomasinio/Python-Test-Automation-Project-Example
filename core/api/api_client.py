from furl import furl
from loguru import logger
from pprint import pformat
from requests import Session, Request

from configuration import SERVICE_URL
from .response import Response


def response_logging_hook(response: Request, *args, **kwargs):
    logger.debug(response.url)
    logger.debug(response.status_code)
    logger.debug("\n" + pformat(response.json()))


class ApiClient:

    def __init__(self, base_url=SERVICE_URL, raise_for_status=True):
        self.base_url = furl(base_url)
        self.session = Session()
        self.session.hooks["response"] = response_logging_hook
        self.raise_for_status = raise_for_status

    def get(self, path="/", params=None):
        url = self.base_url / path
        response = self.session.get(url, params=params)
        if self.raise_for_status:
            response.raise_for_status()
        return Response(response)

    def post(self, path="/", data=None, json=None):
        url = self.base_url / path
        response = self.session.post(url, data, json)
        if self.raise_for_status:
            response.raise_for_status()
        return Response(response)
