from core.api_client import ApiClient
from core.models.post import PostModel

client = ApiClient().authorize()


def test_1():
    response = client.post(path="/games/", data='search "zelda"; where rating >= 80 & release_dates.date > 631152000;')
    response.assert_status_code(200)


# def test_1():
#     response = client.get(path="/posts/1/")
#     response.assert_status_code(200).validate(PostModel)
#     assert response.title == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
#
#
# def test_2():
#     response = client.get(path="/posts/2/")
#     response.assert_status_code(200).validate(PostModel)
