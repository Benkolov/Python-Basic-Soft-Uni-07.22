number_m = int(input())

count = 0
is_password = False
password = ""
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a * b + c * d == number_m:
                    if a < b and c > d:
                        print(f'{a}{b}{c}{d}', end=" ")
                        count += 1
                        if count == 4:
                            is_password = True
                            password += f"{a}{b}{c}{d}"

print()
if 0 <= count < 4:
    print("No!")

if is_password:
    print(f"Password: {password}")