number = int(input())

for i in range(1, 10):
    for k in range(1, 10):
        for j in range(1, 10):
            for z in range(1, 10):
                if i + k == j + z:
                    if number % (i + k) == 0:
                        print(f'{i}{k}{j}{z}', end=" ")