nylon = int(input())
paint = int(input())
razr = int(input())
hours_workers = int(input())

price_nylon = (nylon + 2) * 1.5
price_paint = (paint * 1.1) * 14.5
price_razr = razr * 5
sum_materials = price_nylon + price_paint + price_razr + 0.40

price_hours_workers = (sum_materials * 0.30) * hours_workers

total_sum = sum_materials + price_hours_workers

print(total_sum)

