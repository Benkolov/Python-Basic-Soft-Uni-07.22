import math
tournament = int(input())
start_points = int(input())

total_points = start_points
win = 0


for i in range(1, tournament + 1):
    progress_tour = input()
    if progress_tour == "W":
        total_points += 2000
        win += 1
    elif progress_tour == "F":
        total_points += 1200
    else:
        total_points += 720

diff_point = total_points - start_points
average_points = math.floor(diff_point / tournament)
winning_percent = win / tournament * 100

print(f"Final points: {total_points}")
print(f"Average points: {average_points:}")
print(f"{winning_percent:.2f}%")