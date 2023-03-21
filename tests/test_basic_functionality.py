import allure
import pytest

from src.models.game import GameModel
from src.test_data.query_builder import QueryBuilder
from src.test_data.predefined_data import top_third_person_shooters


@pytest.mark.parametrize("game_name", top_third_person_shooters)
def test_name(authorized_api_client, game_name):
    client = authorized_api_client
    query_builder = QueryBuilder().select_fields().search(game_name).build()

    response = client.games.get_info(query_builder)
    response.assert_status_code([200, 201]).validate(GameModel)
    with allure.step(f"Check that all game names from the response starts with {game_name}"):
        assert all([game.name.title().startswith(game_name) for game in response.items])


@pytest.mark.parametrize("game_name", top_third_person_shooters)
def test_rating(authorized_api_client, game_name):
    client = authorized_api_client
    query_search_game = QueryBuilder().select_fields().search(game_name).build()
    query_search_game_with_rating_filtering = (QueryBuilder().select_fields().search(game_name).
                                               where_rating_more_than(80).build())

    response1 = client.games.get_info(query_search_game)
    response1.assert_status_code(200).validate(GameModel)

    response2 = client.games.get_info(query_search_game_with_rating_filtering)
    response2.assert_status_code(200).validate(GameModel)

    result1 = [game.id for game in response1.items
               if game.rating is not None and game.rating >= 80.0]
    result2 = [game.id for game in response2.items]
    assert result1 == result2, "Wrong elements"
