import math


length = float(input())
width = float(input())

length_cm = length * 100
width_cm = width * 100

workplace_row = math.floor((width_cm - 100) / 70)
workplace_column = math.floor(length_cm / 120)

workplace = (workplace_column * workplace_row) - 3

print(workplace)