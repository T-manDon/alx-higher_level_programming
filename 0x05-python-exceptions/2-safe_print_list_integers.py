#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Initialize a counter for the number of integer elements printed
    # Iterate through the list elements up to the specified number of elements (x)
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")  # Print the integer element
            count += 1  # Increment the counter
        except (ValueError, TypeError):
            pass  # Skip printing if the element is not an integer
    print("")  # Print a newline character after printing elements
