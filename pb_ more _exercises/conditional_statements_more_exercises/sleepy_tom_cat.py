holidays = int(input())

working_days = 365 - holidays

min_to_play = (holidays * 127) + (working_days * 63)

diff = abs(30000 - min_to_play)
hours = diff // 60
minutes = diff - (hours * 60)

if min_to_play > 30000:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')