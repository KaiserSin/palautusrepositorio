import re
from typing import List

import requests


class SeasonReader:
    def __init__(self, url: str = "https://studies.cs.helsinki.fi/nhlstats/"):
        self.url = url
        self.seasons = self.get_seasons()

    def get_seasons(self) -> List[str]:
        response = requests.get(self.url, timeout=10)
        response.raise_for_status()
        match = re.search(
            r"following seasons available\s+([^<]+)",
            response.text,
            flags=re.IGNORECASE,
        )
        if not match:
            raise ValueError("Could not find season information from the response")
        seasons = [season.strip() for season in match.group(1).split(",") if season.strip()]
        if not seasons:
            raise ValueError("Season list was empty")
        return seasons
