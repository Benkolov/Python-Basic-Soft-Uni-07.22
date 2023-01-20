length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = length * width * height

total_lt = volume / 1000
acc_lt = total_lt * (percent / 100)

result = total_lt - acc_lt

print(result)