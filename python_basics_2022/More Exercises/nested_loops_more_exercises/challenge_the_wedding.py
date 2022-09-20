number_man = int(input())
number_woman = int(input())
number_table = int(input())

count = 0

for man in range(1, number_man + 1):
    if count >= number_table:
        break
    for woman in range(1, number_woman + 1):
        print(f"({man} <-> {woman})", end=' ')
        count += 1
        if count >= number_table:
            break