number_km = int(input())
time_of_day = input()

price = 0

if number_km < 20:
    if time_of_day == "day":
        price = 0.70 + (number_km * 0.79)
    else:
        price = 0.70 + (number_km * 0.90)
elif 20 <= number_km < 100:
    price = number_km * 0.09
else:
    price = number_km * 0.06
print(f"{price:.2f}")



