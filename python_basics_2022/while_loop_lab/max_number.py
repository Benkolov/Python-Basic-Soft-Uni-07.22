import sys
max_number = -sys.maxsize
command = input()


while command != "Stop":
    count = int(command)
    if count > max_number:
        max_number = count
    command = input()

print(max_number)



