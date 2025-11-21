first_match_result = input()
second_match_result = input()
third_match_result = input()

won_games = 0
lost_games = 0
drawn_games = 0

home_goals_1 = int(first_match_result[0])
away_goals_1 = int(first_match_result[2])
home_goals_2 = int(second_match_result[0])
away_goals_2 = int(second_match_result[2])
home_goals_3 = int(third_match_result[0])
away_goals_3 = int(third_match_result[2])

if home_goals_1 > away_goals_1:
    won_games += 1
elif home_goals_1 < away_goals_1:
    lost_games += 1
elif home_goals_1 == away_goals_1:
    drawn_games += 1

if home_goals_2 > away_goals_2:
    won_games += 1
elif home_goals_2 < away_goals_2:
    lost_games += 1
elif home_goals_2 == away_goals_2:
    drawn_games += 1

if home_goals_3 > away_goals_3:
    won_games += 1
elif home_goals_3 < away_goals_3:
    lost_games += 1
elif home_goals_3 == away_goals_3:
    drawn_games += 1

print(f'Team won {won_games} games.')
print(f'Team lost {lost_games} games.')
print(f'Drawn games: {drawn_games}')