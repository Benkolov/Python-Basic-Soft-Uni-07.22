number = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(1, number + 1):
    currentNum = int(input())

    if currentNum < 200:
        p1 = p1 + 1
    elif currentNum <= 399:
        p2 = p2 + 1
    elif currentNum <= 599:
        p3 = p3 + 1
    elif currentNum <= 799:
        p4 = p4 + 1
    else:
        p5 = p5 + 1

p1_percent = p1 / number * 100
print(f"{p1_percent:.2f}%")
p2_percent = p2 / number * 100
print(f"{p2_percent:.2f}%")
p3_percent = p3 / number * 100
print(f"{p3_percent:.2f}%")
p4_percent = p4 / number * 100
print(f"{p4_percent:.2f}%")
p5_percent = p5 / number * 100
print(f"{p5_percent:.2f}%")









