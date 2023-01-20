number = int(input())

counter_of_combination = 0

for x1 in range(0, number + 1):
    for x2 in range(number + 1):
        for x3 in range(number + 1):
            if x1 + x2 + x3 == number:
                counter_of_combination += 1
print(counter_of_combination)