#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    # Try to print the integer using the specified format
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err:
        # Print the exception message to stderr and return False
        print("Exception: {}".format(err), file=sys.stderr)
        return False
    else:
        # Return True if printing is successful and no exception occurs
        return True
