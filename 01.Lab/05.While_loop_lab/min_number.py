import sys
min_number = sys.maxsize
command = input()


while command != "Stop":
    count = int(command)
    if count < min_number:
        min_number = count
    command = input()

print(min_number)