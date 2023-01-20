student = int(input())

count_grade = 0
top_student = 0
between_up = 0
between_down = 0
fail_student = 0

for i in range(1, student + 1):
    student_grade = float(input())
    count_grade += student_grade
    if student_grade >= 5:
        top_student += 1
    elif 5 > student_grade >= 4:
        between_up += 1
    elif 4 > student_grade >= 3:
        between_down += 1
    elif student_grade < 3:
        fail_student += 1

average_grade = count_grade / student
percent_top_student = top_student / student * 100
percent_between_up = between_up / student * 100
percent_between_down = between_down / student * 100
percent_fail_student = fail_student / student * 100

print(f"Top students: {percent_top_student:.2f}%")
print(f"Between 4.00 and 4.99: {percent_between_up:.2f}%")
print(f"Between 3.00 and 3.99: {percent_between_down:.2f}%")
print(f"Fail: {percent_fail_student:.2f}%")
print(f"Average: {average_grade:.2f}")
