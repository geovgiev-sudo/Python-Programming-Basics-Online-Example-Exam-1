command = input()
total_matches_played = 0
tournaments_count = 0
matches_won = 0
matches_lost = 0

while command != 'End of tournaments':
    tournament_name = command
    matches_played = int(input())
    total_matches_played += matches_played
    tournaments_count += 1

    for match in range(1, matches_played + 1):

        points_dessi = int(input())
        points_enemy = int(input())

        if points_dessi > points_enemy:
            matches_won += 1
            diff = points_dessi - points_enemy
            print(f'Game {match} of tournament {tournament_name}: win with {diff} points.')

        elif points_dessi < points_enemy:
            matches_lost += 1
            diff = points_enemy - points_dessi
            print(f'Game {match} of tournament {tournament_name}: lost with {diff} points.')

    command = input()


protzent_games_won = matches_won / total_matches_played * 100
protzent_games_lost = matches_lost / total_matches_played * 100
print(f'{protzent_games_won:.2f}% matches win')
print(f'{protzent_games_lost:.2f}% matches lost')
