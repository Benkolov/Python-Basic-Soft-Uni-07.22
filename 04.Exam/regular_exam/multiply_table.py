number = int(input())

first_digit = number % 10
second_digit = number // 10 % 10
third_digit = number // 100 % 10

for num1 in range(1, first_digit + 1):
    for num2 in range(1, second_digit + 1):
        for num3 in range(1, third_digit + 1):
            result = num1 * num2 * num3
            print(f"{num1} * {num2} * {num3} = {result};")

