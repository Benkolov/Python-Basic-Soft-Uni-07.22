price_for_vegetable = float(input())
price_for_fruits = float(input())
kg_vegetable = int(input())
kg_fruits = int(input())


total_price_vege = price_for_vegetable * kg_vegetable
total_price_fruits = price_for_fruits * kg_fruits
total_price = total_price_vege + total_price_fruits
price_in_euro = total_price / 1.94

print(f"{price_in_euro:.2f}")