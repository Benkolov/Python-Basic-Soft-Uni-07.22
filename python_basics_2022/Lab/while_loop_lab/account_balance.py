command = input()

total = 0

while command != "NoMoreMoney":
    payment = float(command)
    if payment < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {payment:.2f}")
    command = input()
    total += payment

print(f"Total: {total:.2f}")
