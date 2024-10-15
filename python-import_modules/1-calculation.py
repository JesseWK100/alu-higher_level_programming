#!/usr/bin/python3
if __name__ == "__main__":
    # Import the functions from calculator_1.py
    from calculator_1 import add, sub, mul, div

    # Define the variables a and b
    a = 10
    b = 5

    # Print the results using f-strings (no .format())
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {sub(a, b)}")
    print(f"{a} * {b} = {mul(a, b)}")
    print(f"{a} / {b} = {div(a, b)}")
