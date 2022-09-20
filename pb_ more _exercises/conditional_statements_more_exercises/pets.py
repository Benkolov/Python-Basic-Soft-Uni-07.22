import math

number_days = int(input())
food_kg = int(input())
food_for_dog_kg = float(input())
food_for_cat_kg = float(input())
food_for_turtle_gr = float(input())

food_for_turtle_kg = food_for_turtle_gr / 1000
total_coast = (food_for_turtle_kg * number_days)\
              + (food_for_cat_kg * number_days)\
              + (food_for_dog_kg * number_days)

if food_kg >= total_coast:
    remainder = math.floor(food_kg - total_coast)
    print(f"{remainder} kilos of food left.")
else:
    lack = math.ceil(total_coast - food_kg)
    print(f'{lack} more kilos of food are needed.')






