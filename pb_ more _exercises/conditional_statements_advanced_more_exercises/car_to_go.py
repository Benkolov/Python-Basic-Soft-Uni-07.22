budget = float(input())
season = input()

class_car = 0
type_car = 0
price_car = 0

if budget <= 100:
    class_car = 'Economy class'
    if season == "Summer":
        type_car = "Cabrio"
        price_car = budget * 0.35
    elif season == "Winter":
        type_car = "Jeep"
        price_car = budget * 0.65
elif 100 < budget <= 500:
    class_car = "Compact class"
    if season == "Summer":
        type_car = "Cabrio"
        price_car = budget * 0.45
    elif season == "Winter":
        type_car = "Jeep"
        price_car = budget * 0.80
elif budget > 500:
    class_car = "Luxury class"
    type_car = 'Jeep'
    price_car = budget * 0.90

print(f"{class_car}")
print(f"{type_car} - {price_car:.2f}")
