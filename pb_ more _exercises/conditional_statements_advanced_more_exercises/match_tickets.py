budget = float(input())
category = input()
members = int(input())

rest_budget = 0
price_ticket = 0

if members < 5:
    rest_budget = budget * 0.25
elif 5 <= members < 10:
    rest_budget = budget * 0.40
elif 10 <= members < 25:
    rest_budget = budget * 0.50
elif 25 <= members < 50:
    rest_budget = budget * 0.60
elif members >= 50:
    rest_budget = budget * 0.75

if category == "VIP":
    price_ticket = 499.99
else:
    price_ticket = 249.99

price_all_ticket = members * price_ticket
diff = abs(rest_budget - price_all_ticket)

if rest_budget >= price_all_ticket:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")



