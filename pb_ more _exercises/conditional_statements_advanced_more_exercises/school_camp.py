season = input()
type_group = input()
number_schoolboy = int(input())
number_overnight_stays = int(input())

price_overnight_stays = 0
type_sport = 0

if season == "Winter":
    if type_group == "boys":
        type_sport = "Judo"
        price_overnight_stays = (number_schoolboy * 9.60) * number_overnight_stays
    elif type_group == "girls":
        type_sport = "Gymnastics"
        price_overnight_stays = (number_schoolboy * 9.60) * number_overnight_stays
    else:
        type_sport = "Ski"
        price_overnight_stays = (number_schoolboy * 10.00) * number_overnight_stays
elif season == "Spring":
    if type_group == "boys":
        type_sport = "Tennis"
        price_overnight_stays = (number_schoolboy * 7.20) * number_overnight_stays
    elif type_group == "girls":
        type_sport = "Athletics"
        price_overnight_stays = (number_schoolboy * 7.20) * number_overnight_stays
    else:
        type_sport = "Cycling"
        price_overnight_stays = (number_schoolboy * 9.50) * number_overnight_stays
else:
    if type_group == "boys":
        type_sport = "Football"
        price_overnight_stays = (number_schoolboy * 15.00) * number_overnight_stays
    elif type_group == "girls":
        type_sport = "Volleyball"
        price_overnight_stays = (number_schoolboy * 15.00) * number_overnight_stays
    else:
        type_sport = "Swimming"
        price_overnight_stays = (number_schoolboy * 20.00) * number_overnight_stays

if number_schoolboy >= 50:
    price_overnight_stays = price_overnight_stays * 0.50
elif 20 <= number_schoolboy < 50:
    price_overnight_stays = price_overnight_stays * 0.85
elif 10 <= number_schoolboy < 20:
    price_overnight_stays = price_overnight_stays * 0.95

print(f"{type_sport} {price_overnight_stays:.2f} lv.")



