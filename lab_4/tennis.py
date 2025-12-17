# -*- coding: utf-8 -*-

class TennisGame1:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_score = 0
        self.p2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1_score += 1
        else:
            self.p2_score += 1

    def score(self):
        if self.p1_score == self.p2_score:
            return self._get_tie_score()
        elif self.p1_score >= 4 or self.p2_score >= 4:
            return self._get_endgame_score()
        else:
            return self._get_running_score()

    def _get_tie_score(self):
        scores = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
        }
        return scores.get(self.p1_score, "Deuce")

    def _get_endgame_score(self):
        minus_result = self.p1_score - self.p2_score
        if minus_result == 1:
            return f"Advantage {self.player1_name}"
        elif minus_result == -1:
            return f"Advantage {self.player2_name}"
        elif minus_result >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def _get_running_score(self):
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        return f"{score_names[self.p1_score]}-{score_names[self.p2_score]}"


class TennisGame2:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_score = 0
        self.p2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1_score += 1
        else:
            self.p2_score += 1

    def score(self):
        if self.p1_score == self.p2_score:
            return self._get_tie_score()

        if self.p1_score >= 4 or self.p2_score >= 4:
            return self._get_endgame_score()

        return self._get_running_score()

    def _get_tie_score(self):
        if self.p1_score > 2:
            return "Deuce"
        score_names = ["Love", "Fifteen", "Thirty"]
        return f"{score_names[self.p1_score]}-All"

    def _get_running_score(self):
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        return f"{score_names[self.p1_score]}-{score_names[self.p2_score]}"

    def _get_endgame_score(self):
        diff = self.p1_score - self.p2_score
        if diff >= 2:
            return f"Win for {self.player1_name}"
        if diff <= -2:
            return f"Win for {self.player2_name}"
        if diff == 1:
            return f"Advantage {self.player1_name}"
        return f"Advantage {self.player2_name}"

    def SetP1Score(self, number):
        self.p1_score = number

    def SetP2Score(self, number):
        self.p2_score = number


class TennisGame3:
    def __init__(self, player1_name, player2_name):
        self.p1_name = player1_name
        self.p2_name = player2_name
        self.p1_score = 0
        self.p2_score = 0

    def won_point(self, name):
        if name == self.p1_name:
            self.p1_score += 1
        else:
            self.p2_score += 1

    def score(self):
        if self.p1_score < 4 and self.p2_score < 4 and (self.p1_score + self.p2_score < 6):
            return self._get_early_game_score()

        if self.p1_score == self.p2_score:
            return "Deuce"

        return self._get_late_game_score()

    def _get_early_game_score(self):
        points_names = ["Love", "Fifteen", "Thirty", "Forty"]
        s = points_names[self.p1_score]
        if self.p1_score == self.p2_score:
            return f"{s}-All"
        return f"{s}-{points_names[self.p2_score]}"

    def _get_late_game_score(self):
        leader = self.p1_name if self.p1_score > self.p2_score else self.p2_name
        is_advantage = abs(self.p1_score - self.p2_score) == 1

        return f"Advantage {leader}" if is_advantage else f"Win for {leader}"