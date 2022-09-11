text = input()

sum_alfabet = 0

for i in range(0, len(text)):
    if text[i] == "a":
        sum_alfabet += 1
    if text[i] == "e":
        sum_alfabet += 2
    if text[i] == "i":
        sum_alfabet += 3
    if text[i] == "o":
        sum_alfabet += 4
    if text[i] == "u":
        sum_alfabet += 5

print(sum_alfabet)




