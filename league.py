
from club import Club

class League:
    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.clubs = []
        self.matches = []

    def add_club(self, club):
        if club not in self.clubs:
            self.clubs.append(club)
        else:
            print("Error. Club already in league.")

    def remove_club(self, club):
        if club in self.clubs:
            self.clubs.remove(club)

    def find_club_by_name(self, club_name):
        for c in self.clubs:
            if c.name == club_name:
                return c
        print("No club found")
        return None
    

    def add_match(self, match):
        self.matches.append(match)
        match.apply_result()

    def get_top_club(self):
        if not self.clubs:
            return None
        else:
            return max(self.clubs, key=lambda club: (club.points, club.get_goal_difference(), club.goals_scored))
            # max finds highest value in a list

    def get_sorted_clubs(self):
        return sorted(self.clubs, key= lambda club: (club.points, club.get_goal_difference(), club.goals_scored), reverse=True)

    def print_table(self):
        sorted_clubs = self.get_sorted_clubs()
        # string formatting %s but with a number to factor it. - means left aligned
        print("%-22s %-5s %-5s %-5s %-5s %-5s %-5s %-5s %-5s" % ("Club", "P", "W", "D", "L", "GF", "GA", "GD", "Pts"))
        # print("-" * 65)
        for club in sorted_clubs:
            print("%-22s %-5s %-5s %-5s %-5s %-5s %-5s %-5s %-5s" % (
                club.name, 
                len(club.match_history), 
                club.wins, 
                club.draws, 
                club.losses, 
                club.goals_scored, 
                club.goals_conceded, 
                club.get_goal_difference(),
                club.points
                ))

    def print_all_clubs(self):
        for club in self.clubs:
            print(club.name)

    def print_all_matches(self):
        for match in self.matches:
            match.print_match_summary() # print_match_summary function already prints itself, so no need to do print() again