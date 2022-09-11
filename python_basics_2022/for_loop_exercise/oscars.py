actor_name = input()
academy_point = float(input())
the_assessors = int(input())

total_points = academy_point

for i in range(1, the_assessors + 1):
    name = input()
    current_points = float(input())

    points = (len(name) * current_points) / 2
    total_points = total_points + points

    if total_points >= 1250.5:
        break

if total_points >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points}!")
else:
    diff = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")

