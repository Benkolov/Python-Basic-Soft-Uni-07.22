num1 = int(input())
num2 = int(input())
num5 = int(input())
profit = int(input())

for one in range(0, num1 + 1):
    for two in range(0, num2 + 1):
        for five in range(0, num5 + 1):
            if one * 1 + two * 2 + five * 5 == profit:
                print(f"{one} * 1 lv. + {two} * 2 lv. + {five} * 5 lv. = {profit} lv.")

