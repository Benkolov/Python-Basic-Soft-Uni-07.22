price_page = float(input())
price_cover = float(input())
percent_discount = int(input())
design_payment = float(input())
percent_pay_from_team = int(input())

price_pages = price_page * 899
price_covers = price_cover * 2
price = (price_pages + price_covers) * (100 - percent_discount) / 100
total_price = (price + design_payment) * (100 - percent_pay_from_team) / 100

print(f"Avtonom should pay {total_price:.2f} BGN.")