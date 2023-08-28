#!/usr/bin/python3
# 100-print_tebahpla.py

# This script prints the alphabet in reverse order, alternating upper- and lower-case letters.

i = 0  # Initialize a variable to alternate between upper- and lower-case

# Iterate through the ASCII values of characters from 'z' to 'a' in reverse
for c in range(ord('z'), ord('a') - 1, -1):
    # Print the character (either upper- or lower-case) based on the value of i
    print("{}".format(chr(c - i)), end="")

    # Toggle the value of i to alternate between upper- and lower-case
    i = 32 if i == 0 else 0
