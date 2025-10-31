import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_search_player(self):
        name = "Lemieux"
        self.assertEqual(self.stats.search(name), Player("Lemieux", "PIT", 45, 54))

    def test_search_nobody(self):
        name = "lol"
        self.assertEqual(self.stats.search(name), None)
    
    def test_team_searching(self):
        players = [Player("Semenko", "EDM", 4, 12), Player("Kurri", "EDM", 37, 53), Player("Gretzky", "EDM", 35, 89)]
        self.assertEqual(self.stats.team("EDM"), players)
    
    def test_top_player(self):
        players = [
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]
        self.assertEqual(self.stats.top(0), players)
