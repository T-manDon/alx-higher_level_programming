#!/usr/bin/python3
import random

# Generate a random integer between -10000 and 10000 (inclusive)
number = random.randint(-10000, 10000)

# Extract the last digit of the absolute value of the number
digit = abs(number) % 10

# If the original number was negative, adjust the sign of the digit
if number < 0:
    digit = -digit

# Print the beginning of the output statement
print("Last digit of {} is {} and is ".format(number, digit), end="")

# Check the value of the extracted digit and provide information accordingly
if digit > 5:
    print("greater than 5")
elif digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
