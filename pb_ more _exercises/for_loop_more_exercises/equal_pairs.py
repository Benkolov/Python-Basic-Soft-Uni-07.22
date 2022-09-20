number_of_pairs = int(input())

sum_of_pairs = list()

for i in range(1, number_of_pairs + 1):
    current_number1 = int(input())
    current_number2 = int(input())
    sum_of_pairs.append(current_number1 + current_number2)

min_of_pairs = sum_of_pairs[0]
max_of_pairs = sum_of_pairs[0]
count = sum_of_pairs[0]
diff_list = list()

for x in sum_of_pairs:
    diff_list.append(abs(count - x))
    count = x
    if x < min_of_pairs:
        min_of_pairs = x
    elif x > max_of_pairs:
        max_of_pairs = x
    if x != count:
        count = x - count

diff = max(diff_list)
if min_of_pairs == max_of_pairs:
    print(f"Yes, value={min_of_pairs}")
else:
    print(f"No, maxdiff={diff}")





