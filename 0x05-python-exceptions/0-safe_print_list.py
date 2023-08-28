#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    num = 0  # Initialize a counter for the number of elements printed

    # Iterate through the list elements up to the specified number of elements (x)
    for i in range(x):
        try:
            print(my_list[i], end="")  # Print the element
            num += 1  # Increment the counter
        except IndexError:
            break  # Break the loop if the index is out of bounds

    print("")  # Print a newline character after printing elements
    return num  # Return the number of elements successfully printed
