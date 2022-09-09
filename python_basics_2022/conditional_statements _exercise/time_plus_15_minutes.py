hours = int(input())
minutes = int(input())

minutes = minutes + 15

if minutes > 59:
    hours = hours + 1
    minutes = minutes - 60

if hours > 23:
    hours = 0

if minutes > 9:
    print(f"{hours}:{minutes}")
else:
    print(f"{hours}:0{minutes}")