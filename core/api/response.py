from pprint import pformat

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
                self.__convert(parsed_object)
        else:
            parsed_object = model.parse_obj(self.response_json)
            self.__convert(parsed_object)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status_code in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status_code == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self

    def __convert(self, parsed_object):
        self.__dict__.update(parsed_object.dict())

    def __repr__(self):
        return pformat({"Response URL": self.response_url,
                        "Response status code": self.response_status_code,
                        "Response JSON body": self.response_json})
