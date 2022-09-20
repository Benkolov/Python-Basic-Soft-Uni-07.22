command = input()

c_counter = 0
o_counter = 0
n_counter = 0
word = ""

while command != "End":
    if 65 <= ord(command) <= 90 or 97 <= ord(command) <= 122:
        if command == 'c':
            if c_counter >= 1:
                word += command
            else:
                c_counter += 1
        elif command == 'o':
            if o_counter >= 1:
                word += command
            else:
                o_counter += 1
        elif command == 'n':
            if n_counter >= 1:
                word += command
            else:
                n_counter += 1
        else:
            word += command
        if c_counter >= 1 and o_counter >= 1 and n_counter >= 1:
            print(f'{word}', end=' ')
            word = ''
            c_counter = 0
            o_counter = 0
            n_counter = 0
    command = input()
