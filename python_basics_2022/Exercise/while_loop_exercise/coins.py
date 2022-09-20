change = float(input())

coins_change = round(change * 100)
count_coins = 0

while coins_change > 0:
    if coins_change >= 200:
        count_coins += 1
        coins_change -= 200
    elif coins_change >= 100:
        count_coins += 1
        coins_change -= 100
    elif coins_change >= 50:
        count_coins += 1
        coins_change -= 50
    elif coins_change >= 20:
        count_coins += 1
        coins_change -= 20
    elif coins_change >= 10:
        count_coins += 1
        coins_change -= 10
    elif coins_change >= 5:
        count_coins += 1
        coins_change -= 5
    elif coins_change >= 2:
        count_coins += 1
        coins_change -= 2
    elif coins_change >= 1:
        count_coins += 1
        coins_change -= 1

print(count_coins)

