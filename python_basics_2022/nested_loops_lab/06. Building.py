number_floors = int(input())
number_room = int(input())

floor_letter = ""

for current_floor in range(number_floors, 0, -1):
    for current_room in range(number_room):
        if current_floor == number_floors:
            floor_letter = "L"
        elif current_floor % 2 == 0:
            floor_letter = "O"
        else:
            floor_letter = "A"
        print(f"{floor_letter}{current_floor}{current_room}", end=" ")
    print()





