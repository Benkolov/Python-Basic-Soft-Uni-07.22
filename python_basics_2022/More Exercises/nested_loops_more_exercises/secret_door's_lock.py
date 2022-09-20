num1 = int(input())
num2 = int(input())
num3 = int(input())

is_real = [2, 3, 5, 7]

for i in range(1, num1 + 1):
    if i % 2 != 0:
        continue
    for k in range(1, num2 + 1):
        if k not in is_real:
            continue
        for j in range(1, num3 + 1):
            if j % 2 != 0:
                continue
            print(f"{i} {k} {j}")