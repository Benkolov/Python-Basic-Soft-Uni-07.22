chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
type_day = input()

price_bucket = 0

if season == 'Spring' or season == 'Summer':
    if type_day == 'Y':
        price_bucket = ((chrysanthemums * 2.00) + (roses * 4.10) + (tulips * 2.50)) * 1.15
    else:
        price_bucket = (chrysanthemums * 2.00) + (roses * 4.10) + (tulips * 2.50)
    if tulips > 7 and (chrysanthemums + roses + tulips) > 20:
        price_bucket = price_bucket * 0.95
        price_bucket = price_bucket * 0.80
    elif tulips > 7:
        price_bucket = price_bucket * 0.95
elif season == 'Autumn' or season == 'Winter':
    if type_day == 'Y':
        price_bucket = ((chrysanthemums * 3.75) + (roses * 4.50) + (tulips * 4.15)) * 1.15
    else:
        price_bucket = (chrysanthemums * 3.75) + (roses * 4.50) + (tulips * 4.15)
    if roses >= 10 and (chrysanthemums + roses + tulips) > 20:
        price_bucket = price_bucket * 0.90
        price_bucket = price_bucket * 0.80
    elif roses >= 10:
        price_bucket = price_bucket * 0.90

total_price = price_bucket + 2

print(f"{total_price:.2f}")





