games = "/games"
game_engines = "/game_engines"


class GameApiClient:

    def __init__(self, client):
        self.client = client
        self.base_url = self.client.base_url
        self.session = self.client.session

    def get_games_info(self, query):
        return self.client.post(path=games, data=query)
