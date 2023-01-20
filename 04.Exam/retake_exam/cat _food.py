number_cat = int(input())

total_food = 0
small_cat = 0
big_cat = 0
very_big_cat = 0

for i in range(1, number_cat + 1):
    food_gr = float(input())
    total_food += food_gr
    if 100 <= food_gr < 200:
        small_cat += 1
    elif 200 <= food_gr < 300:
        big_cat += 1
    elif 300 <= food_gr < 400:
        very_big_cat += 1

price = (total_food / 1000) * 12.45

print(f"Group 1: {small_cat} cats.")
print(f"Group 2: {big_cat} cats.")
print(f"Group 3: {very_big_cat} cats.")
print(f"Price for food per day: {price:.2f} lv.")