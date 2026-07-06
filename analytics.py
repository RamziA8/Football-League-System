# [] used for list
# {} used for dictionary
# () used for other stuff like functions


from sample_data import create_world_cup_2026_league
from player import Player
from club import Club
from football_match import Match
from league import League

def get_all_players(league):
    all_players = []
    for club in league.clubs:
        for player in club.players:
            all_players.append(player)
    return all_players


def group_players_by_position(league):
    positions = {

    }

    players = get_all_players(league)

    for player in players:
        if player.position not in positions:
            # positions.append(player.positions) this is only for lists
            positions[player.position] = []


            # positions = {'defense' : [] }
            # positions {'defense' : ["Ramos"],
            #             'left_wing': [] }

            positions[player.position].append(player.name)

            # positions {'defense' : ["Ramos"] }
            # positions {'defense' : ["Ramos"],
            #             'left_wing': ["2007 ronaldo"] }
        else:
            positions[player.position].append(player.name)
        
    return positions


def group_players_by_club(league: League ):
    clubs = {}
    for club in league.clubs:
        clubs[club.name] = [player.name for  player in club.players]

def get_players_by_position(league, position):
    players = get_all_players(league)
    position_list = []
    for player in players:
        if player.position == position:
            position_list.append(player)
    return position_list


def get_top_scorers(league, limit):
    # we want the top goal scoring players from the entire player list in the world cup league.
    # we need to take all player, and check their goals, and determine who has the highest goals.
    # we then sort the players in order of highest goals scored
    # we then make a limit, so that only some players show, e.g. 5 players

    players = get_all_players(league)
    top_scorers = sorted(players, key= lambda player: (player.goals), reverse=True)
    return top_scorers[:limit]


def sort_players_by_goal_contributions(league):
    players = get_all_players(league)
    return sorted(players, key= lambda player: (player.goals + player.assists, player.goals, player.assists), reverse=True)

def get_best_attacking_club(league):
    if not league.clubs:
        return None
    else:
        return max(league.clubs, key = lambda club: club.goals_scored)


def get_best_defensive_club(league):
    if not league.clubs:
        return None
    else:
        return min(league.clubs, key = lambda club: club.goals_conceded)


def calculate_club_power_score(club):
    return club.points * 3 + club.get_goal_difference() * 2 + club.goals_scored - club.goals_conceded

def get_power_rankings(league):
    return sorted(league.clubs, key = lambda club: calculate_club_power_score(club), reverse = True)

def get_club_recent_form(club, last_n_matches):
    form = []
    recent_matches = club.match_history[-last_n_matches:]
    # for the matches in recent matches, figure out if the club is home or away, then see if they W, D or L
    for match in recent_matches:
        if match.home_club == club:
            goals_for = match.home_goals
            goals_against = match.away_goals
        else:
            goals_for = match.away_goals
            goals_against = match.home_goals
        if goals_for > goals_against:
            form.append("W")
        elif goals_for == goals_against:
            form.append("D")
        else:
            form.append("L")
    return form

def calculate_form_score(form):
    total_score = 0
    for result in form:
        if result == "W":
            total_score += 3
        elif result == "D":
            total_score += 1
        else:
            total_score += 0
    return total_score

def sort_clubs_by_recent_form(league, last_n_matches):
    # for each club, get their recent form over the last n matches, calculate the score from that form, and sort in order
    return sorted(league.clubs, key = lambda club: calculate_form_score(get_club_recent_form(club, last_n_matches)), reverse = True)


def validate_league_table_consistency(league): 
    # this function is a data integrity check to verify the league data is consistent. total scored and conceded must be equal
    # if the total goals scored by the home teams equal the total conceded by the away team, return true
    total_scored = 0
    total_conceded = 0
    for club in league.clubs:
        total_scored += club.goals_scored
        total_conceded += club.goals_conceded
    if total_scored == total_conceded:
        return True
    else:
        return False

def build_position_report(league):
    # for each position (attacker, midfielder, defender, goalkeeper) we want the count, player names, top scorer
    position_dictionary = {}
    positions = group_players_by_position(league)

    for position in positions:
        player_names = positions[position] # get the list of players stored at this position key
        players_in_position = get_players_by_position(league, position)
        top_scorer = max(players_in_position, key = lambda player: player.goals)

        position_dictionary[position] = {
            "count": len(player_names),
            "players": player_names,
            "top_scorer": top_scorer.name
        }
    return position_dictionary

def find_duplicate_shirt_numbers(club):
    shirt_number_seen = []
    duplicate = []
    for player in club.players:
        if player.shirt_number in shirt_number_seen:
            duplicate.append(player.shirt_number)
        else:
            shirt_number_seen.append(player.shirt_number)
    return duplicate

def find_transfer_candidates(league, max_age, min_goals):
    candidates = []
    players = get_all_players(league)
    for player in players:
        if player.age <= max_age and player.goals >= min_goals:
            candidates.append(player)
    return sorted(candidates, key = lambda player: player.goals, reverse = True)    

def recommend_club_improvement(club):
    recommendations = []
    if club.get_goal_difference() < 0:
        recommendations.append("Needs better Attacking/Defending to score more/concede less.")
    if club.wins < club.losses:
        recommendations.append("Bad record. Consider having tactical changes.")
    if not recommendations:
        return "Club is performing well."
    return recommendations

def build_club_report(club):
    return {
        "club name": club.name,
        "city": club.city,
        "club manager": club.manager,
        "number of players": club.get_number_of_players(),
        "average age": club.get_average_age(),
        "goals scored": club.goals_scored,
        "goals conceded": club.goals_conceded,
        "goal difference": club.get_goal_difference(),
        "points": club.points,
        "recent form": get_club_recent_form(club, 5),
        "recommendation": recommend_club_improvement(club)
    }

def build_league_summary(league):
    return {
        "league name": league.name,
        "country": league.country,
        "number of clubs": len(league.clubs),
        "number of players": len(get_all_players(league)),
        "number of matches": len(league.matches),
        "best attacking club": get_best_attacking_club(league).name,
        "best defensive club": get_best_defensive_club(league).name,
        "top scorer": get_top_scorers(league, 1)[0].name,
        "power rankings": [club.name for club in get_power_rankings(league)],
        "table consistency": validate_league_table_consistency(league)
    }