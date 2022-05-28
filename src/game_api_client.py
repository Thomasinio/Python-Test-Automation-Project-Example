import allure

games = "/games"
game_engines = "/game_engines"


class GameApiClient:

    def __init__(self, client):
        self.client = client

    @allure.step("Get games information")
    def get_info(self, query):
        return self.client.post(path=games, data=query)
