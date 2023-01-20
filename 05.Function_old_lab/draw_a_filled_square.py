n = int(input())


def print_dashes(num):
    print("-" * (num * 2))


def print_body(number):
    for i in range(1, number - 1):
        print("-" + "\\/" * int((2 * number - 2) / 2) + "-")


print_dashes(n)
print_body(n)
print_dashes(n)