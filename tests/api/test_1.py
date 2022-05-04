from loguru import logger

from core.api.api_client import ApiClient
from core.api.models.post import PostModel

client = ApiClient()


def test_1():
    response = client.get(path="/posts/1/")
    response.assert_status_code(200).validate(PostModel)
    assert response.title == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"


def test_2():
    response = client.get(path="/posts/2/")
    response.assert_status_code(200).validate(PostModel)
