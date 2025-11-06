from typing import List

from player import Player


class PlayerStats:
    def __init__(self, reader ):
        self.players = reader.players

    def top_scorers_by_nationality(self, nationality: str):
        filtered = [player for player in self.players if player.nationality == nationality]
        if not filtered:
            return [f"No players found for nationality {nationality}."]

        players_sorted = sorted(filtered, key=lambda p: p.goals + p.assists, reverse=True)

        name_width = max(len(player.name) for player in players_sorted)
        team_width = max(len("TEAM"), *(len(player.team) for player in players_sorted))
        points_strings = [
            f"{player.assists} + {player.goals} = {player.assists + player.goals}"
            for player in players_sorted
        ]
        points_width = max(len("POINTS"), *(len(points) for points in points_strings))

        header = (
            f"{'NAME':<{name_width}} | "
            f"{'TEAM':<{team_width}} | "
            f"{'POINTS':<{points_width}}"
        )

        rows = [header]
        for player, points in zip(players_sorted, points_strings):
            rows.append(
                f"{player.name:<{name_width}} | "
                f"{player.team:<{team_width}} | "
                f"{points:>{points_width}}"
            )
        return rows
