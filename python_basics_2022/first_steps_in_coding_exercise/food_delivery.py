chicken_menu_count = int(input())
fish_menu_count = int(input())
veg_menu_count = int(input())

price_chicken = chicken_menu_count * 10.35
price_fish = fish_menu_count * 12.4
price_veg = veg_menu_count * 8.15

all_menu_price = price_chicken + price_fish + price_veg

dessert = all_menu_price * 0.20
total_sum = all_menu_price + dessert + 2.5

print(total_sum)