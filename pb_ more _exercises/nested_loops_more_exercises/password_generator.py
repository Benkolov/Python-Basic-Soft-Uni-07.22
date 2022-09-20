n = int(input())
l = int(input())

for a in range(1, n + 1):
    for b in range(1, n + 1):
        for c in range(1, l + 1):
            c += 96
            for d in range(1, l + 1):
                d += 96
                for e in range(1, n + 1):
                    if e > a and e > b:
                        print(f"{a}{b}{chr(c)}{chr(d)}{e}", end=" ")




