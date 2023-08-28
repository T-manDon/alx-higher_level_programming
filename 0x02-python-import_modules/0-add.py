#!/usr/bin/python3

# Check if this script is being run as the main program
if __name__ == "__main__":
    """Print the sum of 1 and 2."""

    # Import the 'add' function from the 'add_0' module
    from add_0 import add

    # Define the values to be added
    a = 1
    b = 2

    # Print the sum using the 'add' function
    print("{} + {} = {}".format(a, b, add(a, b)))
