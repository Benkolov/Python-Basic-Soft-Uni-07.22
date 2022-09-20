length_space = int(input())
width_space = int(input())
height_space = int(input())

volume_of_space = length_space * width_space * height_space

input_line = input()

sum_boxes = 0

while input_line != "Done":
    boxes = int(input_line)
    sum_boxes += boxes

    if sum_boxes >= volume_of_space:
        break

    input_line = input()

diff = abs(volume_of_space - sum_boxes)
if sum_boxes >= volume_of_space:
    print(f"No more free space! You need {diff} Cubic meters more.")
else:
    print(f"{diff} Cubic meters left.")