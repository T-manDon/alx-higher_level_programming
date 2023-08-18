#!/usr/bin/python3

"""
Print all possible unique combinations of two digits in ascending order.
The two digits must be different; for example, 01 and 10 are considered identical.
"""

for digit1 in range(0, 9):
    for digit2 in range(digit1 + 1, 10):
        print("{}{}".format(digit1, digit2), end=", ")

print("89")  # Print the last combination (8 and 9) without a comma at the end
