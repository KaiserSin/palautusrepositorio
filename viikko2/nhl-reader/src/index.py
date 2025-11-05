import requests

from player import Player

def main():
    players = get_players()
    one_national(players)
    

def get_players():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url)
    players_data = response.json()
    return [Player(player) for player in players_data]

def one_national(players, national = "FIN"):
    print(f"Players from {national}:")
    filtered = [player for player in players if player.nationality == national]

    name_width = max(len(player.name) for player in filtered)
    team_width = max(len("TEAM"), *(len(player.team) for player in filtered))
    assists_width = max(len("ASSISTS"), *(len(str(player.assists)) for player in filtered))
    goals_width = max(len("GOALS"), *(len(str(player.goals)) for player in filtered))
    games_width = max(len("GAMES"), *(len(str(player.games)) for player in filtered))

    header = (
        f"{'NAME':<{name_width}} | "
        f"{'TEAM':<{team_width}} | "
        f"{'ASSISTS':>{assists_width}} | "
        f"{'GOALS':>{goals_width}} | "
        f"{'GAMES':>{games_width}}"
    )

    rows = [header]
    for player in filtered:
        rows.append(
            f"{player.name:<{name_width}} | "
            f"{player.team:<{team_width}} | "
            f"{player.assists:>{assists_width}} | "
            f"{player.goals:>{goals_width}} | "
            f"{player.games:>{games_width}}"
        )
    for row in rows:
        print(row)
    

if __name__ == "__main__":
    main()
