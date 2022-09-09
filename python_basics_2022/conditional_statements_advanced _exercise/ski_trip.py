count_day = int(input())
tip_room = input()
rating = input()

price_room = 0

if tip_room == "room for one person":
    price_room = 18

if tip_room == "apartment":
    if count_day > 15:
        price_room = 25 * 0.5
    elif 10 < count_day < 15:
        price_room = 25 * 0.65
    elif count_day < 10:
        price_room = 25 * 0.70
    else:
        price_room = 25
if tip_room == "president apartment":
    if count_day > 15:
        price_room = 35 * 0.80
    elif 10 < count_day < 15:
        price_room = 35 * 0.85
    elif count_day < 10:
        price_room = 35 * 0.90
    else:
        price_room = 35

total_price = (count_day - 1) * price_room

if rating == "positive":
    print(f"{total_price * 1.25:.2f}")
else:
    print(f"{total_price * 0.9:.2f}")


