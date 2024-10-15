#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Get the last digit
last_digit = number % 10

# Adjust for negative last digits
if number < 0:
    last_digit = -last_digit

# Print the results
print(f"Last digit of {number} is {last_digit}", end=' ')

# Check the value of last_digit and print appropriate message
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
