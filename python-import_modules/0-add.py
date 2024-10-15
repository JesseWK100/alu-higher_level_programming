#!/usr/bin/python3
if __name__ == "__main__":
    # Import the add function from add_0.py (only one occurrence of add_0)
    from add_0 import add

    # Assign values to a and b in two different lines
    a = 1
    b = 2

    # Use string formatting to display the result
    print("{} + {} = {}".format(a, b, add(a, b)))
