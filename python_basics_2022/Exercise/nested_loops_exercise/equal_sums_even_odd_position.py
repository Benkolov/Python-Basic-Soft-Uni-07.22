first_number = int(input())
second_number = int(input())

for current_number in range(first_number, second_number + 1):
    odd_digit_sum = 0
    even_digit_sum = 0
    current_number_as_string = str(current_number)
    for index, digit in enumerate(current_number_as_string):
        if index % 2 == 0:
            odd_digit_sum += int(digit)
        else:
            even_digit_sum += int(digit)
    if odd_digit_sum == even_digit_sum:
        print(current_number, end=" ")
