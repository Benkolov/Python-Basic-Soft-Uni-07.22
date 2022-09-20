number = int(input())

count = 0

for i in range(1, number + 1):
    current_number = int(input())
    count += current_number

print(f'{count / number:.2f}')