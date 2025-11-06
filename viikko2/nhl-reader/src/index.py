from PlayerReader import PlayerReader
from PlayerStats import PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    nationality = "FIN"
    players = PlayerReader(url)
    stats = PlayerStats(players)
    rows = stats.top_scorers_by_nationality(nationality)

    for row in rows:
        print(row)

if __name__ == "__main__":
    main()
