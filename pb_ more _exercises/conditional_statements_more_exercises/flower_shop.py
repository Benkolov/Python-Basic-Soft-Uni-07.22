import math
magnolias_pcs = int(input())
hyacinth_pcs = int(input())
roses_pcs = int(input())
cacti_pcs = int(input())
gift_price = float(input())

order = (magnolias_pcs * 3.25) + (hyacinth_pcs * 4) + (roses_pcs * 3.50) + (cacti_pcs * 8)
order_revenue = order * 0.95

if order_revenue >= gift_price:
    instead = math.floor(order_revenue - gift_price)
    print(f"She is left with {instead} leva.")
else:
    lack = math.ceil(gift_price - order_revenue)
    print(f"She will have to borrow {lack} leva.")






