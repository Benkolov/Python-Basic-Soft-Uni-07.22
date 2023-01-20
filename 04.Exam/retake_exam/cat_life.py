breed_cat = input()
gender_cat = input()

cat_months = 0
result = False

if breed_cat == "British Shorthair":
    result = True
    if gender_cat == "m":
        cat_months = 13 * 2
    elif gender_cat == "f":
        cat_months = 14 * 2
elif breed_cat == "Siamese":
    result = True
    if gender_cat == "m":
        cat_months = 15 * 2
    elif gender_cat == "f":
        cat_months = 16 * 2
elif breed_cat == "Persian":
    result = True
    if gender_cat == "m":
        cat_months = 14 * 2
    elif gender_cat == "f":
        cat_months = 15 * 2
elif breed_cat == "Ragdoll":
    result = True
    if gender_cat == "m":
        cat_months = 16 * 2
    elif gender_cat == "f":
        cat_months = 17 * 2
elif breed_cat == "American Shorthair":
    result = True
    if gender_cat == "m":
        cat_months = 12 * 2
    elif gender_cat == "f":
        cat_months = 13 * 2
elif breed_cat == "Siberian":
    result = True
    if gender_cat == "m":
        cat_months = 11 * 2
    elif gender_cat == "f":
        cat_months = 12 * 2
else:
    print(f"{breed_cat} is invalid cat!")

if result:
    print(f"{cat_months} cat months")





