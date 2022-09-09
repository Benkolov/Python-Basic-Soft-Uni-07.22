mont = input()
count_day = int(input())

price_studio = 0
price_apart = 0

if mont == "May" or mont == "October":
    if count_day > 14:
        price_studio = 50 * 0.70
        price_apart = 65 * 0.90
    elif count_day > 7:
        price_studio = 50 * 0.95
        price_apart = 65
    else:
        price_studio = 50
        price_apart = 65

if mont == "June" or mont == "September":
    if count_day > 14:
        price_studio = 75.20 * 0.80
        price_apart = 68.70 * 0.90
    else:
        price_studio = 75.20
        price_apart = 68.70

if mont == "July" or mont == "August":
    if count_day > 14:
        price_studio = 76.00
        price_apart = 77 * 0.90
    else:
        price_studio = 76.00
        price_apart = 77

total_price_studio = price_studio * count_day
total_price_apart = price_apart * count_day

print(f"Apartment: {total_price_apart:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")