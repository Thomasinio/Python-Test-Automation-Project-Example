from pprint import pformat
from typing import Union, List, Dict

from loguru import logger
from requests import Response
from pydantic.main import ModelMetaclass, ValidationError


class ResponseValidator:

    def __init__(self, response: Response):
        self.response = response
        self.response_url = response.url
        # response.request.body?
        self.response_json = response.json()
        self.response_status_code = response.status_code
        # list() always creates a new object on the heap, but [] can reuse memory cells in many situations
        self.items = list()

    def assert_status_code(self, status_code: Union[int, List[int]]):
        if isinstance(status_code, list):
            assert self.response_status_code in status_code
        else:
            assert self.response_status_code == status_code
        return self

    def validate(self, model: ModelMetaclass):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                self._model_parsing_process(model, item)
        else:
            self._model_parsing_process(model, self.response_json)
        return self

    def _model_parsing_process(self, model: ModelMetaclass, item: Union[List, Dict]):
        try:
            parsed_object = model.parse_obj(item)
            # annoying
            self.items.append(parsed_object)
        except ValidationError:
            # Loguru will automatically add the traceback of occurring exception while using logger.exception()
            logger.exception("\n" + pformat(item))
            raise

    def __repr__(self):
        # self = Response(https://api.igdb.com/v4/games, 200, [{'id': 19, 'age_ratings': [519, 47525], ...}])
        return f"Response({self.response_url}, {self.response_status_code}, {self.response_json})"
