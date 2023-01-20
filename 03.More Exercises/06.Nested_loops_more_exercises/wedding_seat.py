last_sector = input()
number_line_in_first_sector = int(input())
number_seat_in_odd_line = int(input())

number_seat = number_seat_in_odd_line
count = 0
for sector in range(65, ord(last_sector) + 1):
    if sector > 65:
        number_line_in_first_sector += 1
    for line in range(1, number_line_in_first_sector + 1):
        if line % 2 == 0:
            number_seat += 2
        else:
            number_seat = number_seat_in_odd_line
        for seat in range(1, number_seat + 1):
            seat += 96
            print(f"{chr(sector)}{line}{chr(seat)}")
            count += 1
            number_seat = number_seat_in_odd_line

print(count)