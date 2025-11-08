from PlayerReader import PlayerReader
from PlayerStats import PlayerStats
from SeasonReader import SeasonReader
from rich.console import Console
from rich.table import Table
from rich.text import Text


def _prompt(console: Console, text: Text) -> str:
    console.print(text)
    return console.input("> ").strip()


def application():
    console = Console()
    season_reader = SeasonReader()
    seasons = season_reader.seasons
    active_season = "2024-25"

    season_text = Text("Season ", style="bold white")
    season_text.append(f"[{'/'.join(seasons)}]", style="magenta")
    season_text.append(f" ({active_season})", style="bright_cyan")
    entered_season = _prompt(console, season_text)
    if entered_season and entered_season in seasons:
        active_season = entered_season
    url = f"https://studies.cs.helsinki.fi/nhlstats/{active_season}/players"
    player_reader = PlayerReader(url)
    stats = PlayerStats(player_reader)
    default_nat = ("FIN" if "FIN" in player_reader.nationalities else player_reader.nationalities[0])
    active_nationality = default_nat
    while True:
        nationality_text = Text("Nationality ", style="bold white")
        nationality_text.append(f"[{'/'.join(player_reader.nationalities)}]", style="magenta")
        nationality_text.append(f" ({active_nationality})", style="bright_cyan")

        user_input = _prompt(console, nationality_text).upper()
        if user_input in {"Q", "EXIT", "QUIT"}:
            break
        if user_input:
            active_nationality = user_input
        top_players = stats.players_sorted_by_points(active_nationality)
        if not top_players:
            continue

        table = Table(
            title=f"Top scorers ({active_nationality})",
            show_header=True,
            header_style="bold white",
        )
        table.add_column("Name", style="bright_cyan", no_wrap=True)
        table.add_column("Team", style="magenta")
        table.add_column("Goals", justify="right", style="green")
        table.add_column("Assists", justify="right", style="green")
        table.add_column("Points", justify="right", style="bold bright_green")

        for player in top_players:
            table.add_row(
                player.name,
                player.team,
                str(player.goals),
                str(player.assists),
                str(player.goals + player.assists),
            )

        console.print(table)


def main():
    application()


if __name__ == "__main__":
    main()
