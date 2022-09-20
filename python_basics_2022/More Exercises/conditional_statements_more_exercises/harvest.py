import math
import decimal

vineyard_area = int(input())
grape_per_m = float(input())
liters_of_wine_needed = int(input())
number_of_workers = int(input())

grape = (vineyard_area * grape_per_m)
grape_for_wine = grape * 0.4
wine = decimal.Decimal(grape_for_wine / 2.5)
diff = math.floor((abs(wine - liters_of_wine_needed)))

if wine < liters_of_wine_needed:
    print(f"It will be a tough winter! More {diff} liters wine needed.")
else:
    wine_for_workers = math.ceil(diff / number_of_workers)
    print(f"Good harvest this year! Total wine: {wine} liters.")
    print(f'{diff} liters left -> {wine_for_workers} liters per person.')