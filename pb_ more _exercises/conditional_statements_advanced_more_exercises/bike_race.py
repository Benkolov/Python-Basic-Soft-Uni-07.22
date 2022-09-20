juniors = int(input())
seniors = int(input())
race = input()


tax_income = 0

if race == "cross-country":
    if (juniors + seniors) >= 50:
        tax_income = (juniors * (8 * 0.75)) + (seniors * (9.50 * 0.75))
    else:
        tax_income = juniors * 8 + seniors * 9.50
elif race == "trail":
    tax_income = juniors * 5.50 + seniors * 7
elif race == "downhill":
    tax_income = juniors * 12.25 + seniors * 13.75
elif race == "road":
    tax_income = juniors * 20 + seniors * 21.50

money_for_charity = tax_income * 0.95
print(f"{money_for_charity:.2f}")

