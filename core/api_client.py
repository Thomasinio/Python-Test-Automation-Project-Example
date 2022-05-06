from furl import furl
from loguru import logger
from pprint import pformat
from requests import Session, Response as RequestsResponse

from urls import AUTH0_HOST, SERVICE_URL
from .models.auth import AuthDataModel, AuthResponseModel
from .response import Response


def check_for_error(response: RequestsResponse, *args, **kwargs) -> None:
    response.raise_for_status()


def response_logging_hook(response: RequestsResponse, *args, **kwargs) -> None:
    logger.debug(response.url)
    logger.debug(response.status_code)
    logger.debug("\n" + pformat(response.json()))


class ApiClient:

    def __init__(self, base_url: str = SERVICE_URL) -> None:
        self.base_url = furl(base_url)
        self.session = Session()
        # list of functions that are called after every response
        self.session.hooks["response"] = [check_for_error, response_logging_hook]

    def authorize(self, auth_data=AuthDataModel()):
        url = AUTH0_HOST
        token = AuthResponseModel(**self.session.post(url, data=auth_data.dict()).json())
        self.session.headers["Client-ID"] = "qg705rudhk2h7yztnasre9v727ub1p"
        self.session.headers["Authorization"] = f"{token.token_type.capitalize()} {token.access_token}"
        return self

    def get(self, path: str = "/", params=None) -> Response:
        url = self.base_url / path
        response = self.session.get(url, params=params)
        return Response(response)

    def post(self, path: str = "/", data=None, json=None) -> Response:
        url = self.base_url / path
        response = self.session.post(url, data, json)
        return Response(response)
