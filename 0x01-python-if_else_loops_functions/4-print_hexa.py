#!/usr/bin/python3
# 4-print_hexa.py

# This script prints numbers from 0 to 98 in both decimal and hexadecimal representations.

# Iterate through numbers from 0 to 98
for number in range(0, 99):
    # Print the number in decimal and its hexadecimal equivalent
    print("{} = {}".format(number, hex(number)))
