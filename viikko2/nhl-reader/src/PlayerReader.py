import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.players = self.get_players()

    def get_players(self):
        response = requests.get(self.url)
        players_data = response.json()
        return [Player(player) for player in players_data]



