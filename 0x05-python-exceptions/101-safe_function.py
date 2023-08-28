#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try: # Try to call the provided function with the given arguments
        num = fct(*args)
        return num  # Return the result of the function call
    except Exception as err:
        # Print the exception message to stderr and return None
        print("Exception: {}".format(err), file=sys.stderr)
        return None  # Return None if an exception occurs
