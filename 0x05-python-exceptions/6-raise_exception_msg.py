#!/usr/bin/python3
def raise_exception_msg(message=""):
    """Raise a NameError exception with a message."""
    raise NameError(message)

# Test code
try:
    raise_exception_msg("C is fun")  # Call the function with a custom message
except NameError as ne:
    print(ne)  # Print the caught NameError exception and its message
