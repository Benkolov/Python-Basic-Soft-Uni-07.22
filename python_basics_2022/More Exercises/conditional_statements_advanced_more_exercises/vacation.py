budget = float(input())
season = input()


location = 0
accommodation = 0
price = 0

if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.45
elif 1000 < budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.80
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.60
elif budget > 3000:
    accommodation = "Hotel"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.90
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.90

print(f"{location} - {accommodation} - {price:.2f}")



