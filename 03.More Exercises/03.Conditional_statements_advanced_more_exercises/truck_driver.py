season = input()
km_mont = float(input())

salary = 0

if km_mont <= 5000:
    if season == "Spring" or season == "Autumn":
        salary = (km_mont * 0.75) * 4
    elif season == "Summer":
        salary = (km_mont * 0.90) * 4
    elif season == "Winter":
        salary = (km_mont * 1.05) * 4
elif 5000 < km_mont <= 10000:
    if season == "Spring" or season == "Autumn":
        salary = (km_mont * 0.95) * 4
    elif season == "Summer":
        salary = (km_mont * 1.10) * 4
    elif season == "Winter":
        salary = (km_mont * 1.25) * 4
else:
    salary = (km_mont * 1.45) * 4

brute_salary = salary * 0.90

print(f"{brute_salary:.2f}")


