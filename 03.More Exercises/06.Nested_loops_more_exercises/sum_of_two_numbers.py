num1 = int(input())
num2 = int(input())
magic_num = int(input())
number_comb = 0
count_comb = 0
is_magic = True
for i in range(num1, num2 + 1):
    for k in range(num1, num2 + 1):
        count_comb += 1
        if i + k == magic_num:
            is_magic = False
            number_comb = count_comb
            print(f"Combination N:{number_comb} ({i} + {k} = {magic_num})")
            break
    if not is_magic:
        break
if is_magic:
    print(f"{count_comb} combinations - neither equals {magic_num}")