deposit_amount = float(input())
months = int(input())
annual_rate = float(input())
per_year = deposit_amount * (annual_rate / 100)
per_monts = per_year / 12
total_sum = deposit_amount + (months * per_monts)
print(total_sum)