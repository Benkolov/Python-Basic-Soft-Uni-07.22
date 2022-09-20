budget = float(input())
years = int(input())

even = 0
odd = 0
ivan_years = 17
additional_cost = 0

for i in range(1800, years + 1):
    ivan_years += 1
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
        additional_cost += ivan_years * 50

needed_money = (even + odd) * 12000 + additional_cost

diff = abs(budget - needed_money)

if budget >= needed_money:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {diff:.2f} dollars to survive.")