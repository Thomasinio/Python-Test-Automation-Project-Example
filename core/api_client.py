from furl import furl
from loguru import logger
from pprint import pformat
from requests import Session, Response

from .game_api_client import GameApiClient
from .response_validator import ResponseValidator
from .models.auth import AuthDataModel, AuthResponseModel
from core.configs.main_configuration import SERVICE_HOST, AUTH0_HOST, AUTH0_CLIENT_ID


@logger.catch
def check_for_error(response: Response, *args, **kwargs):
    response.raise_for_status()


def response_logging_hook(response: Response, *args, **kwargs):
    logger.debug(response.url)
    logger.debug(response.status_code)
    logger.debug("\n" + pformat(response.json()))


class ApiClient:

    def __init__(self, base_url: furl = SERVICE_HOST):
        self.base_url = base_url
        self.session = Session()
        # List of functions that are called after every response
        self.session.hooks["response"] = [check_for_error, response_logging_hook]
        self.games = GameApiClient(client=self)

    def authorize(self, auth_data: AuthDataModel = AuthDataModel()):
        url = AUTH0_HOST
        token = AuthResponseModel(**self.session.post(url, data=auth_data.dict()).json())
        self.session.headers["Client-ID"] = AUTH0_CLIENT_ID
        self.session.headers["Authorization"] = f"{token.token_type.capitalize()} {token.access_token}"
        return self

    def get(self, path="/", params=None):
        url = self.base_url / path
        response = self.session.get(url, params=params)
        return ResponseValidator(response)

    def post(self, path="/", data=None, json=None):
        url = self.base_url / path
        response = self.session.post(url, data, json)
        return ResponseValidator(response)
