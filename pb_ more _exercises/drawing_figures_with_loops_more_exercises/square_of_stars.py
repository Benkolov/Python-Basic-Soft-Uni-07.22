n = int(input())

for i in range(1, n + 1):
    print("*", end=" ")
    for x in range(1, n):
        print("*", end=" ")
    print()