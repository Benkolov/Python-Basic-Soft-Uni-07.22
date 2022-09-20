bottle = int(input())
command = input()

needed_cleaner = bottle * 750
dishes = 0
pots = 0
num = 0

while command != "End":
    count_wish = int(command)
    num += 1
    if num % 3 == 0:
        needed_cleaner -= count_wish * 15
        pots += count_wish
    else:
        needed_cleaner -= count_wish * 5
        dishes += count_wish
    if needed_cleaner < 0:
        break
    command = input()


if needed_cleaner >= 0:
    print("Detergent was enough!")
    print(f"{dishes} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {needed_cleaner} ml.")
else:
    print(f"Not enough detergent, {abs(needed_cleaner)} ml. more necessary!")
