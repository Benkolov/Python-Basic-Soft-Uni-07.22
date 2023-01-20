year_tax = int(input())

price_kecove = year_tax * 0.60
price_ekip = price_kecove * 0.80
price_topka = price_ekip / 4
price_aksesoar = price_topka / 5

total_sum = year_tax + price_kecove + price_ekip + price_topka + price_aksesoar

print(total_sum)