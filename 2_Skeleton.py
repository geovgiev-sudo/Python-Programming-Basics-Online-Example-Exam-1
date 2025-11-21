minutes = int(input())
seconds = int(input())
length = float(input())
seconds_for_100 = int(input())

kontrola_in_seconds = minutes * 60 + seconds
slow_downs = length / 120
total_slow_down = slow_downs * 2.5
time_marin = (length / 100) * seconds_for_100 - total_slow_down

if time_marin <= kontrola_in_seconds:
    print(f'Marin Bangiev won an Olympic quota!')
    print(f'His time is {time_marin:.3f}.')
else:
    time_needed = time_marin - kontrola_in_seconds
    print(f'No, Marin failed! He was {time_needed:.3f} second slower.')