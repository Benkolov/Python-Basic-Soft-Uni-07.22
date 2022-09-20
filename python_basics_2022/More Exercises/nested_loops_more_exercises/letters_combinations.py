char_1 = input()
char_2 = input()
char_3 = input()
count = 0
for i in range(ord(char_1), ord(char_2) + 1):

    for k in range(ord(char_1), ord(char_2) + 1):
        for j in range(ord(char_1), ord(char_2) + 1):
            if i != ord(char_3):
                if j != ord(char_3):
                    if k != ord(char_3):
                        print(f"{chr(i)}{chr(k)}{chr(j)}", end=" ")
                        count += 1
print(count)





