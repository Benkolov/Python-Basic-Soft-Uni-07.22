type_of_fuel = input()
amount_of_fuel = float(input())

if type_of_fuel == "Diesel":
    type_of_fuel = "diesel"
elif type_of_fuel == "Gasoline":
    type_of_fuel = "gasoline"
elif type_of_fuel == "Gas":
    type_of_fuel = "gas"

if type_of_fuel == "diesel" or type_of_fuel == "gasoline" or type_of_fuel == "gas":
    if amount_of_fuel >= 25:
        print(f"You have enough {type_of_fuel}.")
    else:
        print(f"Fill your tank with {type_of_fuel}!")
else:
    print("Invalid fuel!")

