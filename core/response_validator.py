from typing import TypeVar, Union, List

from requests import Response
from pydantic.main import ModelMetaclass

from core.enums.global_enums import GlobalErrorMessages

Self = TypeVar('Self', bound='ResponseValidator')


class ResponseValidator:

    def __init__(self, response: Response) -> None:
        self.response = response
        self.response_url = response.url
        self.response_json = response.json()
        self.response_status_code = response.status_code

    def assert_status_code(self, status_code: Union[int, List[int]]) -> Self:
        if isinstance(status_code, list):
            assert self.response_status_code in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status_code == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self

    def validate(self, model: ModelMetaclass) -> Self:
        if isinstance(self.response_json, list):
            for item in self.response_json:
                parsed_object = model.parse_obj(item)
                self.__extend_object_attributes_with(parsed_object)
        else:
            parsed_object = model.parse_obj(self.response_json)
            self.__extend_object_attributes_with(parsed_object)
        return self

    def __extend_object_attributes_with(self, parsed_object: ModelMetaclass) -> Self:
        """
        The method provides attribute style access to a response body
        Instead of annoying:
        >>> self.response_json["books"][-1]["name"]
        We can simply write:
        >>> self.response_json.books[-1].name
        """
        self.__dict__.update(parsed_object.dict())
        return self

    def __repr__(self) -> str:
        return f"Response({self.response_url}, {self.response_status_code}, {self.response_json})"
