start_of_interval = int(input())
end_of_interval = int(input())
magic_number = int(input())

counter_of_combination = 0

combination_is_found = False

for first_number in range(start_of_interval, end_of_interval + 1):
    for second_number in range(start_of_interval, end_of_interval + 1):
        counter_of_combination += 1
        if first_number + second_number == magic_number:
            combination_is_found = True
            break
    if combination_is_found:
        break
if combination_is_found:
    print(f"Combination N:{counter_of_combination} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{counter_of_combination} combinations - neither equals {magic_number}")