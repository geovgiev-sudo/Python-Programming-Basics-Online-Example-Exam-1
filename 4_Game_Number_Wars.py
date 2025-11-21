player_one = input()
player_two = input()
player_one_points = 0
player_two_points = 0

command = input()

while command != 'End of game':

    card_one = int(command)
    card_two = int(input())

    if card_one > card_two:
        player_one_points += (card_one - card_two)

    elif card_two > card_one:
        player_two_points += (card_two - card_one)

    elif card_one == card_two:
        print(f'Number wars!')
        card_one = int(input())
        card_two = int(input())
        if card_one > card_two:
            print(f'{player_one} is winner with {player_one_points} points')
            break
        elif card_two > card_one:
            print(f'{player_two} is winner with {player_two_points} points')
            break

    command = input()

else:
    print(f'{player_one} has {player_one_points} points')
    print(f'{player_two} has {player_two_points} points')
