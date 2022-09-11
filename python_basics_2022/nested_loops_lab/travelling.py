destination = input()
# budget = float(input())

while destination != "End":
    needed_money = float(input())
    money_in_hand = 0
    while money_in_hand < needed_money:
        current_money = float(input())
        money_in_hand += current_money
    print(f"Going to {destination}!")
    destination = input()