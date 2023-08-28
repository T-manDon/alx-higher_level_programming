#!/usr/bin/python3
# 6-print_comb3.py

# This script prints all possible different combinations of two digits in ascending order.
# The two digits must be different - 01 and 10 are considered identical.

# Iterate through the first digit from 0 to 9
for digit1 in range(0, 10):
    # Iterate through the second digit from digit1 + 1 to 9
    for digit2 in range(digit1 + 1, 10):
        # Check if the current combination is 89
        if digit1 == 8 and digit2 == 9:
            # If it's 89, print it without a comma and space
            print("{}{}".format(digit1, digit2))
        else:
            # For other combinations, print them with a comma and space
            print("{}{}".format(digit1, digit2), end=", ")
