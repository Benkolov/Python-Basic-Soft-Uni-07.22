v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

total_p1 = p1 * h
total_p2 = p2 * h

total_debit = total_p1 + total_p2

p1_percent = total_p1 * 100 / total_debit
p2_percent = total_p2 * 100 / total_debit
overflows = abs(total_debit - v)
pool_percent = total_debit * 100 / v

if total_debit <= v:
    print(f"The pool is {pool_percent:.2f}% full. Pipe 1: {p1_percent:.2f}%. Pipe 2: {p2_percent:.2f}%.")
else:
    print(f"For {h} hours the pool overflows with {overflows} liters.")