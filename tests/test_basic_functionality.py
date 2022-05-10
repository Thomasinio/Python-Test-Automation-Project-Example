from core.models.game import GameModel


def test_name(authorized_api_client):
    client = authorized_api_client
    query_builder = 'fields *; search "Max Payne";'

    response = client.games.get_info(query_builder)
    response.assert_status_code(200).validate(GameModel)
    assert all([game.name.startswith("Max Payne") for game in response.items])
