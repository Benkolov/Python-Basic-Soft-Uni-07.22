import math
name_series = input()
duration_series = int(input())
duration_break = int(input())

time_breakfast = duration_break / 8
time_rest = duration_break / 4
time_to_watch = duration_break - (time_breakfast + time_rest)
diff = abs(time_to_watch - duration_series)
rounded = math.ceil(diff)
if time_to_watch >= duration_series:
    print(f"You have enough time to watch {name_series} and left with {rounded} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_series}, you need {rounded} more minutes.")