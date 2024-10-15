#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Get the last digit
last_digit = abs(number) % 10  # Use abs to get the last digit

# Print the results
print(f"Last digit of {number} is", end=' ')

# Check the value of last_digit and print appropriate message
if number < 0:
    print(f"-{last_digit}", end=' ')  # Ensure to print negative last digit
else:
    print(last_digit, end=' ')

# Conditional check for last digit
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
