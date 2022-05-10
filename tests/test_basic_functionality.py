from core.models.game import GameModel


def test_name(authorized_game_api_client):
    client = authorized_game_api_client
    query_builder = 'fields *; search "Max Payne";'

    response = client.get_games_info(query_builder)
    response.assert_status_code(200).validate(GameModel)
    assert all([game.name.startswith("Max Payne") for game in response.items])
