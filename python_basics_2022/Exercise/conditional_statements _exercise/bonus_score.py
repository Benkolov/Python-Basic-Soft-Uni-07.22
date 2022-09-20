point = int(input())
bonus_point = 0

if point <= 100:
    bonus_point = 5

elif point < 1000:
    bonus_point = point * 0.20
else:
    bonus_point = point * 0.10
if point % 2 == 0:
    bonus_point = bonus_point + 1
elif point % 10 == 5:
    bonus_point = bonus_point + 2
print(bonus_point)
print(bonus_point + point)
