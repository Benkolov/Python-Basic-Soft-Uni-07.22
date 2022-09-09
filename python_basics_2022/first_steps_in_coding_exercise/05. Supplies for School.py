pen_count = int(input())
marker_count = int(input())
detergent_lt = int(input())
discount_percent = int(input())

price_pen = pen_count * 5.80
price_markers = marker_count * 7.20
price_detergent = detergent_lt * 1.20
all_price = price_pen + price_markers + price_detergent

discount = all_price * (discount_percent/100)
total_price = all_price - discount
print(total_price)