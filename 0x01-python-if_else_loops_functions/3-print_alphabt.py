#!/usr/bin/python3

# Iterate through the ASCII values of lowercase letters (97 to 122)
for letter in range(97, 123):
    # Check if the character is not 'q' and not 'e'
    if chr(letter) is not 'q' and chr(letter) is not 'e':
        # Print the character without newline
        print("{}".format(chr(letter)), end="")
