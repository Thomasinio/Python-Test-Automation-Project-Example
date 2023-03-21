from furl import furl
from requests import Session

from src.game_api_client import GameApiClient
from src.response_validator import ResponseValidator
from src.models.auth import AuthDataModel, AuthResponseModel
from src.configs.main_configuration import SERVICE_HOST, AUTH0_HOST, AUTH0_CLIENT_ID, TIMEOUT_THRESHOLD
from src.requests_hooks import check_for_error, response_logging_hook


class ApiClient:

    def __init__(self, base_url: furl = SERVICE_HOST):
        self.base_url = base_url
        # Creating a Session instance allows us to store headers, cookies, and authentication across all HTTP requests made with that session
        self.session = Session()
        # Configure hooks for the session that are called after every response
        self.session.hooks["response"] = [check_for_error, response_logging_hook]
        self.games = GameApiClient(client=self)

    def configure_session(self, config: dict):
        for key, value in config.items():
            setattr(self.session, key, value)

    def authorize(self, auth_data: AuthDataModel = AuthDataModel()):
        url = AUTH0_HOST
        token = AuthResponseModel(**self.post(url, data=auth_data.dict()).response_json)
        self.session.headers["Client-ID"] = AUTH0_CLIENT_ID
        self.session.headers["Authorization"] = f"{token.token_type.capitalize()} {token.access_token}"
        return self

    def _request(self, method, path: [str, furl], **kwargs):
        if "://" in str(path):
            # Path is already a complete URL
            url = path
        else:
            # Path is a relative path that needs to be combined with the base URL
            url = self.base_url / path
        response = self.session.request(method, url, timeout=TIMEOUT_THRESHOLD, **kwargs)
        return ResponseValidator(response)

    def get(self, path="/", **kwargs):
        return self._request("GET", path, **kwargs)

    def post(self, path="/", **kwargs):
        return self._request("POST", path, **kwargs)

    def put(self, path="/", **kwargs):
        return self._request("PUT", path, **kwargs)

    def patch(self, path="/", **kwargs):
        return self._request("PATCH", path, **kwargs)

    def delete(self, path="/", **kwargs):
        return self._request("DELETE", path, **kwargs)
