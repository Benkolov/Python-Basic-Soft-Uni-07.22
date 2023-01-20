degree = float(input())

if 26 <= degree <= 35:
    print("Hot")
elif 20 < degree < 26:
    print("Warm")
elif 15 <= degree <= 20:
    print("Mild")
elif 12 <= degree < 15:
    print("Cool")
elif 5 <= degree < 12:
    print("Cold")
else:
    print("unknown")