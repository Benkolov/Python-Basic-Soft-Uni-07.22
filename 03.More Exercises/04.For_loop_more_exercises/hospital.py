days = int(input())


treated_patients = 0
untreated_patients = 0
number_doctor = 7

for i in range(1, days + 1):
    patients = int(input())
    if i % 3 == 0 and treated_patients <= untreated_patients:
        number_doctor += 1
    if patients <= number_doctor:
        treated_patients += patients
    else:
        treated_patients += number_doctor
        untreated_patients += patients - number_doctor

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")




