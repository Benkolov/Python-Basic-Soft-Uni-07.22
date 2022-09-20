mont = int(input())

electricity = 0
water = 0
internet = 0

for i in range(1, mont + 1):
    electricity_bill = float(input())
    electricity += electricity_bill
    water += 20
    internet += 15

other = (electricity + water + internet) * 1.20
total = electricity + water + internet + other
average = total / mont

print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {average:.2f} lv")



