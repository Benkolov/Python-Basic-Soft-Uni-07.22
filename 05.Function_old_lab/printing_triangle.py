n = int(input())


def print_triangle(num):
    for line in range(1, num + 1):
        for column in range(1, line + 1):
            print(f"{column}", end="")
        print()
    for i in range(num - 1, 0, - 1):
        for column in range(1, i + 1):
            print(f"{column}", end="")
        print()


print_triangle(n)
