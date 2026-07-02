from player import Player
from club import Club
from football_match import Match
from league import League
from utils import print_title

# -------------------------
# Create clubs
# -------------------------

real_madrid = Club("Real Madrid", "Madrid", "Carlo Ancelotti")
barcelona = Club("Barcelona", "Barcelona", "Hansi Flick")
man_city = Club("Manchester City", "Manchester", "Pep Guardiola")

# -------------------------
# Create players
# -------------------------

ramzi = Player("Ramzi", 19, 1.75, 72, "Forward")
sanad = Player("Sanad", 24, 1.70, 75, "Midfielder")
ahmad = Player("Ahmad", 20, 1.80, 78, "Defender")
omar = Player("Omar", 22, 1.82, 80, "Goalkeeper")
ali = Player("Ali", 21, 1.77, 74, "Winger")

# -------------------------
# Assign shirt numbers
# -------------------------

ramzi.assign_shirt_number(8)
sanad.assign_shirt_number(9)
ahmad.assign_shirt_number(4)
omar.assign_shirt_number(1)
ali.assign_shirt_number(11)

# -------------------------
# Sign players for clubs
# -------------------------

ramzi.sign_for_club(real_madrid)
sanad.sign_for_club(real_madrid)
ahmad.sign_for_club(barcelona)
omar.sign_for_club(barcelona)
ali.sign_for_club(man_city)

# -------------------------
# Print player information
# -------------------------

print_title("Player Information")

ramzi.print_info()
sanad.print_info()
ahmad.print_info()
omar.print_info()
ali.print_info()

# -------------------------
# Print club players
# -------------------------

print_title("Club Players")

print("Real Madrid players:")
real_madrid.print_players()
print("Barcelona players:")
barcelona.print_players()
print("Manchester City players:")
man_city.print_players()

# -------------------------
# Create league
# -------------------------

champions_league = League("Mini Champions League", "Europe")

champions_league.add_club(real_madrid)
champions_league.add_club(barcelona)
champions_league.add_club(man_city)

# -------------------------
# Print league clubs
# -------------------------

print_title("Champions League Clubs")
champions_league.print_all_clubs()

print_title("Club Summaries Before Matches")
real_madrid.print_summary()
barcelona.print_summary()
man_city.print_summary()

# -------------------------
# Create matches
# -------------------------

match1 = Match(real_madrid, barcelona, 2, 1)
match2 = Match(barcelona, man_city, 1, 1)
match3 = Match(man_city, real_madrid, 2, 6)

# -------------------------
# Add matches to league
# -------------------------

champions_league.add_match(match1)
champions_league.add_match(match2)
champions_league.add_match(match3)

# -------------------------
# Print match summaries
# -------------------------

print_title("Match Results")
champions_league.print_all_matches()

print_title("Club Summaries After Matches")
real_madrid.print_summary()
barcelona.print_summary()
man_city.print_summary()

# -------------------------
# Print league table
# -------------------------

print_title("Champions League Table")
champions_league.print_table()

# -------------------------
# Print top club
# -------------------------

print_title("Top Club")
print("Top Club: ", champions_league.get_top_club().name)