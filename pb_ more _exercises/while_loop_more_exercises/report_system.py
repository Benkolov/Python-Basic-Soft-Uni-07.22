needed_sum = int(input())
command = input()

collected_money = 0
count_pay = 0
cs_sum = 0
cc_sum = 0
cs_transaction = 0
cc_transaction = 0

while command != "End":
    sales = int(command)
    count_pay += 1
    if count_pay % 2 != 0:
        if sales <= 100:
            collected_money += sales
            cs_sum += sales
            cs_transaction += 1
            print("Product sold!")
        else:
            print("Error in transaction!")
    elif count_pay % 2 == 0:
        if sales >= 10:
            collected_money += sales
            cc_sum += sales
            cc_transaction += 1
            print("Product sold!")
        else:
            print("Error in transaction!")
    if collected_money >= needed_sum:
        print(f"Average CS: {cs_sum / cs_transaction:.2f}")
        print(f"Average CC: {cc_sum / cc_transaction:.2f}")
        break
    command = input()

if command == "End":
    print("Failed to collect required money for charity.")