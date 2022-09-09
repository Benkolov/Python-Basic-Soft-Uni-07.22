numOne = int(input())
numTwo = int(input())
operator = input()

result = 0
if operator == "+":
    result = numOne + numTwo
    if result % 2 == 0:
        print(f"{numOne} + {numTwo} = {result} - even")
    else:
        print(f"{numOne} + {numTwo} = {result} - odd")
elif operator == "-":
    result = numOne - numTwo
    if result % 2 == 0:
        print(f"{numOne} - {numTwo} = {result} - even")
    else:
        print(f"{numOne} - {numTwo} = {result} - odd")
elif operator == "*":
    result = numOne * numTwo
    if result % 2 == 0:
        print(f"{numOne} * {numTwo} = {result} - even")
    else:
        print(f"{numOne} * {numTwo} = {result} - odd")
elif operator == "/" and numTwo != 0:
    result = numOne / numTwo
    print(f"{numOne} / {numTwo} = {result:.2f}")
elif operator == "%" and numTwo != 0:
    result = numOne % numTwo
    print(f"{numOne} % {numTwo} = {result}")

if numTwo == 0 and (operator == "/" or operator == "%"):
    print(f"Cannot divide {numOne} by zero")