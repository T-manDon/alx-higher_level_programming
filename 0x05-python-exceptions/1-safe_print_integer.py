#!/usr/bin/python3

def safe_print_integer(value):
    # Try to print the integer using the specified format
    try:
        print("{:d}".format(value))
        return True  # Return True if printing is successful
    except (ValueError, TypeError):
        return False  # Return False if a ValueError or TypeError occurs
