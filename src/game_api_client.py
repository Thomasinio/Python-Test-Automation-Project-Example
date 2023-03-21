import allure


class GameApiClient:

    games = "/games"
    game_engines = "/game_engines"

    def __init__(self, client):
        self.client = client

    @allure.step("Get games information")
    def get_info(self, search_query):
        return self.client.post(path=self.games, data=search_query)
