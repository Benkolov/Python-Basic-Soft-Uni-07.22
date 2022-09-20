failed = int(input())

count_grade = 0
count_bad_grade = 0
sum_grade = 0
last_task = ""

input_line = input()
while input_line != "Enough":
    grade = int(input())
    sum_grade += grade
    last_task = input_line
    count_grade += 1
    if grade <= 4:
        count_bad_grade += 1
    if count_bad_grade == failed:
        break


    input_line = input()

average_grade = sum_grade / count_grade

if count_bad_grade < failed:
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {count_grade}")
    print(f"Last problem: {last_task}")
else:
    print(f"You need a break, {count_bad_grade} poor grades.")














# print(f"You need a break, {брой незадоволителни оценки} poor grades.")
