number_of_cargo = int(input())

price_cargo = 0
van_tonnage = 0
truck_tonnage = 0
train_tonnage = 0

for i in range(1, number_of_cargo + 1):
    tonnage_of_cargo = int(input())
    if tonnage_of_cargo <= 3:
        van_tonnage += tonnage_of_cargo
        price_cargo += 200 * tonnage_of_cargo
    elif 4 <= tonnage_of_cargo <= 11:
        truck_tonnage += tonnage_of_cargo
        price_cargo += 175 * tonnage_of_cargo
    else:
        train_tonnage += tonnage_of_cargo
        price_cargo += 120 * tonnage_of_cargo

total_tonnage = van_tonnage + truck_tonnage + train_tonnage
average_price_per_ton = price_cargo / total_tonnage

print(f"{average_price_per_ton:.2f}")
percent_van = van_tonnage / total_tonnage * 100
percent_truck = truck_tonnage / total_tonnage * 100
percent_train = train_tonnage / total_tonnage * 100
print(f"{percent_van:.2f}%")
print(f"{percent_truck:.2f}%")
print(f"{percent_train:.2f}%")





















