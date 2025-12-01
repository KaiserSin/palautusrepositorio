class TennisGame:
    POINT_NAMES = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
    DEUCE_THRESHOLD = 3
    ADVANTAGE_THRESHOLD = 4
    ADVANTAGE_MARGIN = 1

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_points += 1
            return
        elif player_name == self.player2_name:
            self.player2_points += 1
            return
        else:
            raise ValueError(f"Invalid player name: {player_name}")

    def get_score(self):
        if self._scores_are_tied():
            return self._tied_score()
        if self._either_player_ready_to_win():
            return self._advantage_or_win_score()
        return self._standard_score()

    def _scores_are_tied(self):
        return self.player1_points == self.player2_points

    def _either_player_ready_to_win(self):
        return (
            self.player1_points >= self.ADVANTAGE_THRESHOLD
            or self.player2_points >= self.ADVANTAGE_THRESHOLD
        )

    def _tied_score(self):
        if self.player1_points >= self.DEUCE_THRESHOLD:
            return "Deuce"
        return f"{self._point_name(self.player1_points)}-All"

    def _advantage_or_win_score(self):
        point_difference = self.player1_points - self.player2_points
        if abs(point_difference) == self.ADVANTAGE_MARGIN:
            return f"Advantage {self._leader_name()}"
        return f"Win for {self._leader_name()}"

    def _leader_name(self):
        return self.player1_name if self.player1_points > self.player2_points else self.player2_name

    def _standard_score(self):
        player1_score = self._point_name(self.player1_points)
        player2_score = self._point_name(self.player2_points)
        return f"{player1_score}-{player2_score}"

    def _point_name(self, point_total):
        return self.POINT_NAMES.get(point_total, "Unknown")
