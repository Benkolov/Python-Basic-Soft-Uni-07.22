count_groups = int(input())

musala_sum = 0
montblanc_sum = 0
kilimanjaro_sum = 0
k2_sum = 0
everest_sum = 0
total_sum = 0
for i in range(1, count_groups + 1):
    people = int(input())
    total_sum = total_sum + people

    if people <= 5:
        musala_sum = musala_sum + people
    elif people <= 12:
        montblanc_sum = montblanc_sum + people
    elif people <= 25:
        kilimanjaro_sum = kilimanjaro_sum + people
    elif people <= 40:
        k2_sum = k2_sum + people
    else:
        everest_sum = everest_sum + people

percent_musala = musala_sum / total_sum * 100
print(f"{percent_musala:.2f}%")
percent_montblanc = montblanc_sum / total_sum * 100
print(f"{percent_montblanc:.2f}%")
percent_kilimanjaro = kilimanjaro_sum / total_sum * 100
print(f"{percent_kilimanjaro:.2f}%")
percent_k2 = k2_sum / total_sum * 100
print(f"{percent_k2:.2f}%")
percent_everest = everest_sum / total_sum * 100
print(f"{percent_everest:.2f}%")



