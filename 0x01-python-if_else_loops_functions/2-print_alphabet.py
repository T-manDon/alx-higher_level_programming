#!/usr/bin/python3
# 2-print_alphabet.py

# This script prints the lowercase alphabet characters without newline characters.

# Iterate through the ASCII values of lowercase letters (97 to 122)
for letter in range(97, 123):
    # Convert the ASCII value to the corresponding character and print it
    print("{}".format(chr(letter)), end="")
