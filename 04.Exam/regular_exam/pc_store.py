price_spu = float(input())
price_video_card = float(input())
price_ram = float(input())
number_ram = int(input())
discount = float(input())

discount = discount * 100

price_spu_in_bgn = price_spu * 1.57
price_video_card_in_bgn = price_video_card * 1.57
price_ram_in_bgn = price_ram * 1.57

price_spu_in_bgn = price_spu_in_bgn * (100 - discount) / 100
price_video_card_in_bgn = price_video_card_in_bgn * (100 - discount) / 100

total_price = price_spu_in_bgn + price_video_card_in_bgn + (price_ram_in_bgn * number_ram)

print(f"Money needed - {total_price:.2f} leva.")