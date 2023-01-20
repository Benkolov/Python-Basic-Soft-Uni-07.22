number = int(input())

result = 0
from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
invalid_number = 0

for i in range(1, number + 1):
    current_number = int(input())
    if 0 <= current_number <= 9:
        result += current_number * 0.2
        from_0_to_9 += 1
    elif 10 <= current_number <= 19:
        result += current_number * 0.3
        from_10_to_19 += 1
    elif 20 <= current_number <= 29:
        result += current_number * 0.4
        from_20_to_29 += 1
    elif 30 <= current_number <= 39:
        result += 50
        from_30_to_39 += 1
    elif 40 <= current_number <= 50:
        result += 100
        from_40_to_50 += 1
    else:
        result = result / 2
        invalid_number += 1

percent_from_0_to_9 = from_0_to_9 / number * 100
percent_from_10_to_19 = from_10_to_19 / number * 100
percent_from_20_to_29 = from_20_to_29 / number * 100
percent_from_30_to_39 = from_30_to_39 / number * 100
percent_from_40_to_50 = from_40_to_50 / number * 100
percent_invalid_number = invalid_number / number * 100


print(f"{result:.2f}")
print(f"From 0 to 9: {percent_from_0_to_9:.2f}%")
print(f"From 10 to 19: {percent_from_10_to_19:.2f}%")
print(f"From 20 to 29: {percent_from_20_to_29:.2f}%")
print(f"From 30 to 39: {percent_from_30_to_39:.2f}%")
print(f"From 40 to 50: {percent_from_40_to_50:.2f}%")
print(f"Invalid numbers: {percent_invalid_number:.2f}%")