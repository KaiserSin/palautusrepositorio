class Player:
    def __init__(self, name, team, goals, assists):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists

    @property
    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name} {self.team} {self.goals} + {self.assists} = {self.points}"

    def __eq__(self, other):
        return (
            self.name == other.name
            and self.team == other.team
            and self.goals == other.goals
            and self.assists == other.assists
        )
