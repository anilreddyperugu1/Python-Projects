import os

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def divide(a,b):
    return a/b

symbols = {
    "+": add,
    "-":sub,
    "*": mul,
    "/":divide
}


def calculator():
    number1 = int(input("Enter a number: "))
    for i in symbols.keys():
        print(i)
    to_continue = True
    while to_continue:
        op_symbol = input("Enter an operation: ")
        number2 = int(input("Enter second number: "))
        operation = symbols[op_symbol]
        result=operation(number1,number2)
        print(f"{number1}{op_symbol}{number2}={result}")
        decision = input(f"Type 'y' to continue calculation with {result} (or) 'n' to start fresh (or) 'x' to exit: ").lower()
        if decision == "y":
            to_continue = True
            number1=result
        elif decision == "n":
            os.system("cls")
            calculator()
        elif decision == "x":
            to_continue = False
            print("bye")
            break


calculator()