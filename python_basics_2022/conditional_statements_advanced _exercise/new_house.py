#"Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus"
type_flower = input()
count_flowers = int(input())
budget = int(input())

expenses = 0
if type_flower == "Roses":
    expenses = 5 * count_flowers
    if count_flowers > 80:
        expenses = expenses * 0.90
elif type_flower == "Dahlias":
    expenses = 3.80 * count_flowers
    if count_flowers > 90:
        expenses = expenses * 0.85
elif type_flower == "Tulips":
    expenses = 2.80 * count_flowers
    if count_flowers > 80:
        expenses = expenses * 0.85
elif type_flower == "Narcissus":
    expenses = 3 * count_flowers
    if count_flowers < 120:
        expenses = expenses * 1.15
elif type_flower == "Gladiolus":
    expenses = 2.50 * count_flowers
    if count_flowers < 80:
        expenses = expenses * 1.20

diff = abs(budget - expenses)
if budget >= expenses:
    print(f"Hey, you have a great garden with {count_flowers} {type_flower} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")