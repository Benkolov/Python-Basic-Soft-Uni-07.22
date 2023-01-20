number_days = int(input())
type_room = input()
rating = input()

number_overnight_stay = number_days - 1
price_overnight_stay = 0
total_price = 0

if type_room == "room for one person":
    price_overnight_stay = 18
    total_price = price_overnight_stay * number_overnight_stay
elif type_room == "apartment":
    price_overnight_stay = 25
    total_price = price_overnight_stay * number_overnight_stay
    if number_days > 15:
        total_price = total_price * 0.50
    elif 10 <= number_days <= 15:
        total_price = total_price * 0.65
    elif number_days < 10:
        total_price = total_price * 0.70
elif type_room == "president apartment":
    price_overnight_stay = 35
    total_price = price_overnight_stay * number_overnight_stay
    if number_days > 15:
        total_price = total_price * 0.80
    elif 10 <= number_days <= 15:
        total_price = total_price * 0.85
    elif number_days < 10:
        total_price = total_price * 0.90

if rating == "positive":
    total_price = total_price * 1.25
elif rating == "negative":
    total_price = total_price * 0.90

print(f"{total_price:.2f}")

