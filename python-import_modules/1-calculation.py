#!/usr/bin/python3
if __name__ == "__main__":
    # Import all functions from calculator_1.py
    import calculator_1

    # Define the variables a and b
    a = 10
    b = 5

    # Print the results using f-strings (no .format())
    print(f"{a} + {b} = {calculator_1.add(a, b)}")
    print(f"{a} - {b} = {calculator_1.sub(a, b)}")
    print(f"{a} * {b} = {calculator_1.mul(a, b)}")
    print(f"{a} / {b} = {calculator_1.div(a, b)}")
