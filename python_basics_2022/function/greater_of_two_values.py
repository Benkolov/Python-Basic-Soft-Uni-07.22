input_type = input()
value_1 = input()
value_2 = input()


def get_greater_value(i_t, v_1, v_2):
    result = None
    if i_t == "int":
        if int(v_1) > int(v_2):
            result = v_1
        elif int(v_1) < int(v_2):
            result = v_2
        else:
            result = v_1
    elif i_t == "chr":
        if ord(v_1) > ord(v_2):
            result = v_1
        elif ord(v_1) < ord(v_2):
            result = v_2
        else:
            result = v_1
    else:
        if len(v_1) > len(v_2):
            result = v_1
        elif len(v_1) < len(v_2):
            result = v_2
        else:
            result = v_1
    return result


print(get_greater_value(input_type, value_1, value_2))