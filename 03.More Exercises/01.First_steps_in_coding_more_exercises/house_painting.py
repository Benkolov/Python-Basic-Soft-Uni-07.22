height_house = float(input())
length_house = float(input())
height_triangle = float(input())

beck_wall = height_house * height_house
front_wall = beck_wall - (1.2 * 2)
side_wall = (height_house * length_house) - (1.5 * 1.5)
area_the_wall = beck_wall + front_wall + (side_wall * 2)
consumption_of_green_paint = area_the_wall / 3.4

side_roof = (height_house * length_house)
triangle_roof = (height_house * height_triangle / 2)
area_roof = (side_roof * 2) + (triangle_roof * 2)
consumption_of_red_paint = area_roof / 4.3

print(f"{consumption_of_green_paint:.2f}")
print(f"{consumption_of_red_paint:.2f}")