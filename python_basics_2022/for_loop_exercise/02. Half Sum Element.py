import sys

number = int(input())

max_num = -sys.maxsize
sum_number = 0

for i in range(0, number):
    num = int(input())
    if num > max_num:
        max_num = num
    sum_number += num

if max_num == sum_number - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    sum_number = sum_number - max_num
    print(f"Diff = {abs(max_num - sum_number)}")



