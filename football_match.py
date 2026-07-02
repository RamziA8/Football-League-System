class Match:
    def __init__(self, home_club, away_club, home_goals, away_goals):
        self.home_club = home_club
        self.away_club = away_club
        self.home_goals = home_goals
        self.away_goals = away_goals
        self.result = (home_goals, away_goals)
        self.result_applied = False

    def apply_result(self):
        if self.result_applied == True:
            print("This result has already been applied.")
            return
        else:
            self.home_club.goals_scored += self.home_goals
            self.home_club.goals_conceded += self.away_goals
            self.away_club.goals_scored += self.away_goals
            self.away_club.goals_conceded += self.home_goals
            self.home_club.update_record_after_match(self.home_goals, self.away_goals)
            self.away_club.update_record_after_match(self.away_goals, self.home_goals)
            self.home_club.add_match_to_history(self) # (self) because the inside match.py the current match object is self
            self.away_club.add_match_to_history(self)
            self.result_applied = True

    def get_winner(self):
        if self.home_goals > self.away_goals:
            return self.home_club
        elif self.away_goals > self.home_goals:
            return self.away_club
        else:
            return None

    def is_draw(self):
        if self.home_goals == self.away_goals:
            return True
        else:
            return False

    def get_result_text(self):
        return "%s %s - %s %s" % (self.home_club.name, self.home_goals, self.away_goals, self.away_club.name)

    def print_match_summary(self):
        print(self.get_result_text())
        if self.is_draw():
            print("Result: Draw")
        else:
            print("Winner: ", self.get_winner().name)

    def to_dict(self):
        return {
            "home club": self.home_club.name,
            "away club": self.away_club.name,
            "home goals": self.home_goals,
            "away goals": self.away_goals,
            "result": self.result,
            "Winner": self.get_winner().name if self.get_winner() else "Draw",
            "result applied": self.result_applied
        }