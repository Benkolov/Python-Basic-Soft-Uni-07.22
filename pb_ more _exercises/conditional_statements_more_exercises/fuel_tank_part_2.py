type_of_fuel = input()
amount_of_fuel = float(input())
club_card = input()

fuel_price = 0

if type_of_fuel == "Gas":
    if club_card == "Yes":
        fuel_price = amount_of_fuel * (0.93 - 0.08)
    else:
        fuel_price = amount_of_fuel * 0.93
elif type_of_fuel == "Diesel":
    if club_card == "Yes":
        fuel_price = amount_of_fuel * (2.33 - 0.12)
    else:
        fuel_price = amount_of_fuel * 2.33
elif type_of_fuel == "Gasoline":
    if club_card == "Yes":
        fuel_price = amount_of_fuel * (2.22 - 0.18)
    else:
        fuel_price = amount_of_fuel * 2.22

if amount_of_fuel > 25:
    fuel_price = fuel_price * 0.90
elif 20 <= amount_of_fuel <= 25:
    fuel_price = fuel_price * 0.92

print(f"{fuel_price:.2f} lv.")





