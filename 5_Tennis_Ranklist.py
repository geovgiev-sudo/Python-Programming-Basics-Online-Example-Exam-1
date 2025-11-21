from math import floor

tournaments_count = int(input())
starting_points = int(input())
points = 0
wins = 0

for i in range(1, tournaments_count + 1):
    stage_reached = input()
    if stage_reached == 'W':
        points += 2000
        wins += 1
    elif stage_reached == 'F':
        points += 1200
    elif stage_reached == 'SF':
        points += 720

total_points = points + starting_points
average_points = points / tournaments_count
protzent_wins = wins / tournaments_count * 100

print(f'Final points: {total_points}')
print(f'Average points: {floor(average_points)}')
print(f'{protzent_wins:.2f}%')