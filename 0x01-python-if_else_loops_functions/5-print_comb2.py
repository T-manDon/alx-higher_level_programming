#!/usr/bin/python3

# Iterate through numbers from 0 to 99
for number in range(0, 100):
    # Check if the number is 99
    if number == 99:
        # If the number is 99, print it without a comma and space
        print("{}".format(number))
    else:
        # For other numbers, print them with leading zerosr)
        print("{:02}".format(number), end=", ")
