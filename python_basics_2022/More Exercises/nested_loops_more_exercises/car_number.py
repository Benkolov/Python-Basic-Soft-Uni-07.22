num1 = int(input())
num2 = int(input())

for i in range(num1, num2 + 1):
    for k in range(num1, num2 + 1):
        for j in range(num1, num2 + 1):
            for z in range(num1, num2 + 1):
                if i % 2 == 0 and z % 2 != 0 and i > z and (k + j) % 2 == 0:
                    print(f"{i}{k}{j}{z}", end=" ")
                elif i % 2 != 0 and z % 2 == 0 and i > z and (k + j) % 2 == 0:
                    print(f"{i}{k}{j}{z}", end=" ")
                else:
                    continue