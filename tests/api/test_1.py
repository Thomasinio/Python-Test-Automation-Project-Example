from core.api.api_client import ApiClient
from core.api.enums.global_enums import GlobalErrorMessages
from core.api.models.post import PostModel

api_client = ApiClient()


def test_1():
    response = api_client.get(path="/posts/1/")
    response.assert_status_code(201).validate(PostModel)

