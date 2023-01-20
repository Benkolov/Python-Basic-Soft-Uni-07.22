bachelorette_party_price = float(input())
number_of_love_messages = int(input())
number_of_wax_roses = int(input())
number_of_key_chains = int(input())
number_of_cartoons = int(input())
number_of_lucky_surprises = int(input())

price_number_of_love_messages = number_of_love_messages * 0.60
price_number_of_wax_roses = number_of_wax_roses * 7.20
price_number_of_key_chains = number_of_key_chains * 3.60
price_number_of_cartoons = number_of_cartoons * 18.20
price_number_of_lucky_surprises = number_of_lucky_surprises * 22

income = price_number_of_love_messages + price_number_of_wax_roses + price_number_of_key_chains\
         + price_number_of_cartoons + price_number_of_lucky_surprises
count = number_of_love_messages + number_of_wax_roses + number_of_key_chains\
        + number_of_cartoons + number_of_lucky_surprises
if count >= 25:
    income = income * 0.65
income = income * 0.90
diff = abs(income - bachelorette_party_price)
if income >= bachelorette_party_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")


