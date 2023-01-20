age = int(input())
price_washing_machine = float(input())
price_toy = int(input())

toys_pcs = 0
money = 10
sum_gift = 0
brother_count = 0

for i in range(1, age + 1):
    if i % 2 != 0:
        toys_pcs += 1
    else:
        brother_count += 1
        sum_gift = sum_gift + money
        money = money + 10

result = sum_gift + (toys_pcs * price_toy) - brother_count

diff = abs(result - price_washing_machine)
if result >= price_washing_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")

