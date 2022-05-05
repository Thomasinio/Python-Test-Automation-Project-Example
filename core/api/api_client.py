from furl import furl
from loguru import logger
from pprint import pformat
from requests import Session, Response as RequestsResponse

from urls import SERVICE_URL
from .response import Response


def check_for_error(response: RequestsResponse, *args, **kwargs) -> None:
    response.raise_for_status()


def response_logging_hook(response: RequestsResponse, *args, **kwargs) -> None:
    logger.debug(response.url)
    logger.debug(response.status_code)
    logger.debug("\n" + pformat(response.json()))


class ApiClient:
    """
    Simplified API client
    Initialized with the base URL to which requests will go
    """
    def __init__(self, base_url: str = SERVICE_URL) -> None:
        self.base_url = furl(base_url)
        self.session = Session()
        # list of functions that are called after every response
        self.session.hooks["response"] = [check_for_error, response_logging_hook]

    def get(self, path: str = "/", params=None) -> Response:
        url = self.base_url / path
        response = self.session.get(url, params=params)
        return Response(response)

    def post(self, path: str = "/", data=None, json=None) -> Response:
        url = self.base_url / path
        response = self.session.post(url, data, json)
        return Response(response)
