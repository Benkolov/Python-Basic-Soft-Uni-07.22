import math
record_sec = float(input())
distance_m = float(input())
time_sec_for_1m = float(input())

total_time = distance_m * time_sec_for_1m
delay = math.floor(distance_m / 15) * 12.5
total_time = total_time + delay

if total_time < record_sec:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    diff = total_time - record_sec
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
