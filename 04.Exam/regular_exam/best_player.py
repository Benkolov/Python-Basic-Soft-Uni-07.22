name_player = input()

best_player = 0
best_player_score = 0
while name_player != "END":
    player_score = int(input())
    if player_score > best_player_score:
        best_player_score = player_score
        best_player = name_player
    if player_score >= 10:
        break
    name_player = input()

print(f"{best_player} is the best player!")
if best_player_score >= 3:
    print(f"He has scored {best_player_score} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_player_score} goals.")