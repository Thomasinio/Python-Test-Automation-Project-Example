from furl import furl
from loguru import logger
from pprint import pformat
from requests import Session, Response

from .game_api_client import GameApiClient
from .response_validator import ResponseValidator
from .models.auth import AuthDataModel, AuthResponseModel
from src.configs.main_configuration import SERVICE_HOST, AUTH0_HOST, AUTH0_CLIENT_ID, TIMEOUT_THRESHOLD


def check_for_error(response: Response, *args, **kwargs):
    # Each response is checked that the response HTTP status code is not a 4xx or a 5xx
    response.raise_for_status()


def response_logging_hook(response: Response, *args, **kwargs):
    logger.debug(response.url)
    logger.debug(response.status_code)
    logger.debug("\n" + pformat(response.json()))


class ApiClient:

    def __init__(self, base_url: furl = SERVICE_HOST):
        self.base_url = base_url
        self.session = Session()
        # Configure hooks for the session that are called after every response
        self.session.hooks["response"] = [check_for_error, response_logging_hook]
        self.games = GameApiClient(client=self)

    def configure_session(self, config: dict):
        for key, value in config.items():
            setattr(self.session, key, value)

    def authorize(self, auth_data: AuthDataModel = AuthDataModel()):
        url = AUTH0_HOST
        token = AuthResponseModel(**self.session.post(url, data=auth_data.dict(), timeout=TIMEOUT_THRESHOLD).json())
        self.session.headers["Client-ID"] = AUTH0_CLIENT_ID
        self.session.headers["Authorization"] = f"{token.token_type.capitalize()} {token.access_token}"
        return self

    def request(self, method, path, **kwargs):
        url = self.base_url / path
        response = self.session.request(method, url, **kwargs)
        return ResponseValidator(response)

    def get(self, path="/", **kwargs):
        return self.request("GET", path, **kwargs)

    def post(self, path="/", **kwargs):
        return self.request("POST", path, **kwargs)

    def put(self, path="/", **kwargs):
        return self.request("PUT", path, **kwargs)

    def patch(self, path="/", **kwargs):
        return self.request("PATCH", path, **kwargs)

    def delete(self, path="/", **kwargs):
        return self.request("DELETE", path, **kwargs)
