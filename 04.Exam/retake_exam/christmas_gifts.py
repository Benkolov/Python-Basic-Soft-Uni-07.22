command = input()

number_kids = 0
number_adults = 0

while command != "Christmas":
    age = int(command)
    if age <= 16:
        number_kids += 1
    elif age > 16:
        number_adults += 1
    command = input()

money_for_toys = number_kids * 5
money_for_sweaters = number_adults * 15
total_money = money_for_toys + money_for_sweaters

print(f"Number of adults: {number_adults}" )
print(f"Number of kids: {number_kids}")
print(f"Money for toys: {money_for_toys}")
print(f"Money for sweaters: {money_for_sweaters}")