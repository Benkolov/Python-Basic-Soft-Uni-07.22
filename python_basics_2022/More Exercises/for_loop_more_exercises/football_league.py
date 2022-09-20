stadium_capacity = int(input())
number_of_fans = int(input())

sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for i in range(1, number_of_fans + 1):
    sector = input()
    if sector == 'A':
        sector_a += 1
    elif sector == 'B':
        sector_b += 1
    elif sector == 'G':
        sector_g += 1
    elif sector == 'V':
        sector_v += 1

percent_fans_a = sector_a / number_of_fans * 100
percent_fans_b = sector_b / number_of_fans * 100
percent_fans_v = sector_v / number_of_fans * 100
percent_fans_g = sector_g / number_of_fans * 100
percent_all_fans = number_of_fans / stadium_capacity * 100

print(f"{percent_fans_a:.2f}%")
print(f"{percent_fans_b:.2f}%")
print(f"{percent_fans_v:.2f}%")
print(f"{percent_fans_g:.2f}%")
print(f"{percent_all_fans:.2f}%")