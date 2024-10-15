#!/usr/bin/python3
if __name__ == "__main__":
    # Import the add function from add_0.py
    from add_0 import add

    # Assign values to a and b
    a = 1
    b = 2

    # Print the result in the required format
    print("{} + {} = {}".format(a, b, add(a, b)))
