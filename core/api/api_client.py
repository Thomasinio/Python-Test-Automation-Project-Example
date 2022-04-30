import requests
from furl import furl

from configuration import SERVICE_URL
from .response import Response


class ApiClient:

    def __init__(self, base_url=SERVICE_URL):
        self.base_url = furl(base_url)

    def get(self, path="/", params=None):
        url = self.base_url / path
        response = requests.get(url, params=params)
        return Response(response)

    def post(self, path="/", data=None, json=None):
        url = self.base_url / path
        response = requests.post(url, data, json)
        return Response(response)
