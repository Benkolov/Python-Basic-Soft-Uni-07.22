budget_movie = float(input())
number_extras = int(input())
price_clothing_one = float(input())

decor_price = budget_movie * 0.1
all_clothes_price = number_extras * price_clothing_one

if number_extras > 150:
    all_clothes_price = all_clothes_price * 0.90


total_expenses = decor_price + all_clothes_price

diff = abs(total_expenses - budget_movie)
if budget_movie >= total_expenses:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
