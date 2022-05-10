from typing import Union, List

from requests import Response
from pydantic.main import ModelMetaclass

from core.enums.global_enums import GlobalErrorMessages


class ResponseValidator:

    def __init__(self, response: Response):
        self.response = response
        self.response_url = response.url
        self.response_json = response.json()
        self.response_status_code = response.status_code
        self.items = list()

    def assert_status_code(self, status_code: Union[int, List[int]]):
        if isinstance(status_code, list):
            assert self.response_status_code in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status_code == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self

    def validate(self, model: ModelMetaclass):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                parsed_object = model.parse_obj(item)
                self.items.append(parsed_object)
        else:
            parsed_object = model.parse_obj(self.response_json)
            self.items.append(parsed_object)
        return self

    def __repr__(self):
        return f"Response({self.response_url}, {self.response_status_code}, {self.response_json})"
