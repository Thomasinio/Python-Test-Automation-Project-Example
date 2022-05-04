from pydantic.main import Model

from core.api.enums.global_enums import GlobalErrorMessages


class Response:

    def __init__(self, response):
        self.response = response
        self.response_url = response.url
        self.response_json = response.json()
        self.response_status_code = response.status_code

    def validate(self, model):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                parsed_object = model.parse_obj(item)
                self.__extend_object_attributes_with(parsed_object)
        else:
            parsed_object = model.parse_obj(self.response_json)
            self.__extend_object_attributes_with(parsed_object)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status_code in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status_code == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self

    def __extend_object_attributes_with(self, parsed_object: Model) -> None:
        """
        The method provides attribute style access to a response body.
        Instead of:
        >>> self.response_json["books"][-1]["name"]
        You can simply write:
        >>> self.response_json.books[-1].name
        """
        self.__dict__.update(parsed_object.dict())

    def __repr__(self):
        return f"Response({self.response_url}, {self.response_status_code}, {self.response_json})"
