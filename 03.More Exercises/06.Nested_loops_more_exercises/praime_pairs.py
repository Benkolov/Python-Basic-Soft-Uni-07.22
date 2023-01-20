import math

first_initial_value = int(input())
second_initial_value = int(input())
first_final_value = int(input())
second_final_value = int(input())

for a in range(first_initial_value, first_initial_value + first_final_value + 1):
    is_prime_a = True
    for prime in range(2, int(math.sqrt(a) + 1)):
        if a % prime == 0:
            is_prime_a = False
    for b in range(second_initial_value, second_initial_value + second_final_value + 1):
        is_prime_b = True
        for prime2 in range(2, int(math.sqrt(b) + 1)):
            if b % prime2 == 0:
                is_prime_b = False
        if is_prime_a and is_prime_b:
            print(f"{a}{b}")
