from sample_data import create_world_cup_2026_league
from utils import print_title
from analytics import (
    get_all_players,
    group_players_by_position,
    group_players_by_club,
    get_top_scorers,
    sort_players_by_goal_contributions,
    get_power_rankings,
    calculate_club_power_score,
    get_club_recent_form,
    validate_league_table_consistency,
    build_position_report,
    build_league_summary,
)

world_cup = create_world_cup_2026_league()

print_title("World Cup 2026 Table")
world_cup.print_table()

print_title("All Players Count")
all_players = get_all_players(world_cup)
print(len(all_players))

print_title("Top 5 Scorers")
for player in get_top_scorers(world_cup, 5):
    print(player.name, "-", player.goals, "goals")

print_title("Goal Contributions Ranking")
for player in sort_players_by_goal_contributions(world_cup)[:10]:
    print(player.name, "-", player.goals + player.assists, "contributions")

print_title("Power Rankings")
for club in get_power_rankings(world_cup):
    print(club.name, "-", calculate_club_power_score(club))

print_title("Recent Form")
for club in world_cup.clubs:
    print(club.name, get_club_recent_form(club, 3))

print_title("Table Consistency")
print(validate_league_table_consistency(world_cup))

print_title("League Summary")
print(build_league_summary(world_cup))