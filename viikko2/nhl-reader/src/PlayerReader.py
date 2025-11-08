import requests
from player import Player


class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.players = self.get_players()
        self.teams = self.get_teams()
        self.nationalities = self.get_nationalities()

    def get_players(self):
        response = requests.get(self.url, timeout=10)
        response.raise_for_status()
        players_data = response.json()
        return [Player(player) for player in players_data]

    def get_teams(self):
        return list({player.team for player in self.players})

    def get_nationalities(self):
        return list({player.nationality for player in self.players})


