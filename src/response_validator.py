from pprint import pformat
from typing import Union, List, Dict

from loguru import logger
from requests import Response
from pydantic import BaseModel, ValidationError


class ResponseValidator:

    def __init__(self, response: Response):
        self.response = response
        self.response_url = response.url
        self.response_headers = response.headers
        self.response_json = response.json()
        self.response_status_code = response.status_code
        # list() always creates a new object on the heap, but [] can reuse memory cells in many situations
        self.items = list()

    def assert_headers(self, header: str, value: str):
        assert header in self.response_headers, f"Header {header} not found in response headers: {self.response_headers}"
        assert self.response_headers[header] == value, f"Header {header} has value: {self.response_headers[header]}, expected: {value}"
        return self

    def assert_status_code(self, status_code: Union[int, List[int]]):
        if isinstance(status_code, list):
            assert self.response_status_code in status_code, \
                f"Expected status code to be one of {status_code}, but got {self.response_status_code}."
        else:
            assert self.response_status_code == status_code, \
                f"Expected status code to be {status_code}, but got {self.response_status_code}."
        return self

    def validate(self, model: BaseModel):
        items = self.response_json if isinstance(self.response_json, list) else [self.response_json]
        self.items = [self._parse_item(model, item) for item in items]
        return self

    @staticmethod
    def _parse_item(model: BaseModel, item: Union[List, Dict]):
        try:
            return model.parse_obj(item)
        except ValidationError:
            # Loguru will automatically add the traceback of occurring exception while using logger.exception()
            logger.exception("\n" + pformat(item))
            raise

    def __repr__(self):
        # self = Response(https://api.igdb.com/v4/games, 200, [{'id': 19, 'age_ratings': [519, 47525], ...}])
        return f"Response({self.response_url}, {self.response_status_code}, {self.response_json})"
