class Club:
    def __init__(self, name, city, manager):
        self.name = name
        self.city = city
        self.manager = manager

        self.players = []
        self.goals_scored = 0
        self.goals_conceded = 0

        self.points = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0

        self.match_history = []

    def add_player(self, player):
        # in this case, player is inside the brackets because self refers to the club itself
        # so we want to add the 'player' to the club
        if player not in self.players:
            self.players.append(player)
        else:
            print("Error. Player already in the Club.")

    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)

    # p is player        
    def find_player_by_name(self, player_name):
        for p in self.players:
            if p.name == player_name:
                return p # if a player is found, the function hits return p and exits immmediately so it wouldnt reach statement below
        print("No player found.")
        return None

    def score_goal(self, opponent_club):
        self.goals_scored += 1
        opponent_club.goals_conceded += 1

    def concede_goal(self):
        self.goals_conceded += 1

    def add_match_to_history(self, match):
        self.match_history.append(match)

    def get_goal_difference(self):
        return self.goals_scored - self.goals_conceded

    def get_number_of_players(self):
        return len(self.players) # returns the number of players

    def get_average_age(self):
        if len(self.players) == 0:
            return 0
        ages = [player.age for player in self.players]
        return sum(ages) / len(self.players)

    def update_record_after_match(self, goals_for, goals_against):
        if goals_for > goals_against:
            self.wins += 1
            self.points += 3
        elif goals_for == goals_against:
            self.draws += 1
            self.points += 1
        else:
            self.losses += 1

    def print_players(self):
        if len(self.players) == 0:
            print("There are no players in this club.")
        else:
            for player in self.players:
                print("-", player.name)

    def print_summary(self):
        print("Club Name: ", self.name)
        print("City: ", self.city)
        print("Manager: ", self.manager)
        print("Number of players: ", self.get_number_of_players())
        print("Goals scored: ", self.goals_scored)
        print("Goals conceded: ", self.goals_conceded)
        print("Goal difference: ", self.get_goal_difference())
        print("Points: ", self.points)
        print("Wins: ", self.wins)
        print("Draws: ", self.draws)
        print("Losses: ", self.losses)
        print("Matches played: ", len(self.match_history))

    def to_dict(self):
        return{
            "name": self.name,
            "city": self.city,
            "manager": self.manager,
            "player": [player.name for player in self.players],
            "goals_scored": self.goals_scored,
            "goals_conceded": self.goals_conceded,
            "goal_difference": self.get_goal_difference(),
            "points": self.points,
            "wins": self.wins,
            "draws": self.draws,
            "losses": self.losses,
            "matches_played": len(self.match_history)
        }