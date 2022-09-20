number_days = int(input())
number_hours = int(input())

total_count = 0
day_count = 0
for day in range(1, number_days + 1):
    for hour in range(1, number_hours + 1):
        if day % 2 != 0 and hour % 2 == 0:
            day_count += 1.25
        elif day % 2 == 0 and hour % 2 != 0:
            day_count += 2.50
        else:
            day_count += 1
    print(f"Day: {day} - {day_count:.2f} leva")
    total_count += day_count
    day_count = 0

print(f"Total: {total_count:.2f} leva")