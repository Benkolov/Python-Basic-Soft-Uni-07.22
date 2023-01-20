number_location = int(input())


for location in range(1, number_location + 1):
    expected_yield = float(input())
    numer_days = int(input())
    total_yield = 0
    for days in range(1, numer_days + 1):
        real_yield = float(input())
        total_yield += real_yield
    if total_yield >= expected_yield * numer_days:
        average_yield = total_yield / numer_days
        print(f"Good job! Average gold per day: {average_yield:.2f}.")
    elif total_yield < expected_yield * numer_days:
        average_yield_yield = total_yield / numer_days
        deficit_yield = expected_yield - average_yield_yield
        print(f"You need {deficit_yield:.2f} gold.")


