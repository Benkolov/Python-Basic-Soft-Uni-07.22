a = int(input())
b = int(input())
max_number_pass = int(input())

count = 0
is_end = False

for A in range(35, 56):
    for B in range(64, 97):
        for x in range(1, a + 1):
            for y in range(1, b + 1):
                print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}", end="|")
                A += 1
                B += 1
                if A > 55:
                    A = 35
                if B > 96:
                    B = 64
                count += 1
                if count >= max_number_pass:
                    is_end = True
                    break
                if x == a and y == b:
                    is_end = True
                    break
            if is_end:
                break
        if is_end:
            break
    if is_end:
        break
