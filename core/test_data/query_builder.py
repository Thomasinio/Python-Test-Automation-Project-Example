from typing import List
from loguru import logger


class QueryBuilder:

    def __init__(self):
        self.result = []

    def select_fields(self, fields: List[str] = None):
        if not fields:
            self.result.append("fields *;")
        else:
            self.result.append(f"fields {', '.join(fields)};")
        return self

    def search(self, name: str):
        self.result.append(f"search \"{name}\";")
        return self

    def where_rating_less_than(self, value):
        self.result.append(f"where rating < {value};")
        return self

    def where_rating_more_than(self, value):
        self.result.append(f"where rating > {value};")
        return self

    def build(self):
        built_query_object = ''.join(self.result)
        logger.debug(f"Built result of {self.__class__.__name__} instance: {built_query_object}")
        return built_query_object
