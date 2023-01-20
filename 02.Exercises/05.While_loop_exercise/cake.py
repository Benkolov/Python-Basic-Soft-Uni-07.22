length_cake = int(input())
width_cake = int(input())
input_line = input()

size_cake = length_cake * width_cake

no_more_pieces = False

while input_line != "STOP":
    current_pieces = int(input_line)
    size_cake -= current_pieces

    if size_cake <= 0:
        no_more_pieces = True
        break

    input_line = input()

if no_more_pieces:
    print(f"No more cake left! You need {abs(size_cake)} pieces more.")
else:
    print(f"{abs(size_cake)} pieces are left.")
