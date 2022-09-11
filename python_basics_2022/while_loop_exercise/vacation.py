needed_money = float(input())
owned_money = float(input())

all_days_count = 0
count_spend_days = 0
total_money = owned_money

while total_money < needed_money:
    if count_spend_days == 5:
        break
    action = input()
    amount = float(input())
    all_days_count += 1

    if action == "spend":
        count_spend_days += 1
        total_money -= amount
        if total_money < 0:
            total_money = 0
    elif action == "save":
        count_spend_days = 0
        total_money += amount

if count_spend_days == 5:
    print("You can't save the money.")
    print(f"{all_days_count}")
else:
    print(f"You saved the money for {all_days_count} days.")



