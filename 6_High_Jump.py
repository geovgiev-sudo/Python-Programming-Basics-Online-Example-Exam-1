desired_height = int(input())
initial_height = desired_height - 30
new_height = initial_height
jumps_count = 0
successful_jumps = 0
unsuccessful_jumps = 0

while True:
    height_jumped = int(input())
    jumps_count += 1

    if height_jumped > new_height:
        unsuccessful_jumps = 0
        if new_height == desired_height:
            print(f'Tihomir succeeded, he jumped over {new_height}cm after {jumps_count} jumps.')
            break
        new_height += 5
        successful_jumps += 1

    elif height_jumped <= new_height:
        unsuccessful_jumps += 1
        if unsuccessful_jumps == 3:
            print(f'Tihomir failed at {new_height}cm after {jumps_count} jumps.')
            break