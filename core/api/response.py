from pprint import pformat

from core.api.enums.global_enums import GlobalErrorMessages


class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status_code = response.status_code

    def validate(self, model):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                model.parse_obj(item)
        else:
            model.parse_obj(self.response_json)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status_code in status_code, self
        else:
            assert self.response_status_code == status_code, self
        return self

    def __repr__(self):
        return (f"\nRequested URL: {self.response.url}" 
                f"\nStatus code: {self.response_status_code}" 
                f"\nBody: \n{pformat(self.response_json)}")
