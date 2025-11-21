player_name = input()
points_total = 301
successful_shots = 0
unsuccessful_shots = 0

command = input()

while command != 'Retire':

    field = str(command)
    points = int(input())

    if field == 'Single':
        if points > points_total:
            unsuccessful_shots += 1
        else:
            successful_shots += 1
            points_total -= points

    elif field == 'Double':
        double_points = points * 2
        if double_points > points_total:
            unsuccessful_shots += 1
        else:
            successful_shots += 1
            points_total -= double_points

    elif field == 'Triple':
        triple_points = points * 3
        if triple_points > points_total:
            unsuccessful_shots += 1
        else:
            successful_shots += 1
            points_total -= triple_points

    if points_total == 0:
        print(f'{player_name} won the leg with {successful_shots} shots.')
        break

    command = input()

else:
    print(f'{player_name} retired after {unsuccessful_shots} unsuccessful shots.')