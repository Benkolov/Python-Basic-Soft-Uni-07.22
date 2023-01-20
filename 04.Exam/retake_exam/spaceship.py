import math
width_ship = float(input())
length_ship = float(input())
height_ship = float(input())
average_height_astro = float(input())

capacity_ship = width_ship * length_ship * height_ship
capacity_floor = (average_height_astro + 0.40) * 2 * 2
place_for_astro = math.floor(capacity_ship / capacity_floor)

if 3 <= place_for_astro <= 10:
    print(f"The spacecraft holds {place_for_astro} astronauts.")
elif place_for_astro < 3:
    print("The spacecraft is too small.")
else:
    print("The spacecraft is too big.")