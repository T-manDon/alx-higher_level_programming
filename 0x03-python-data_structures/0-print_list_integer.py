#!/usr/bin/python3

def print_list_integer(my_list=None):
    """Print all integers of a list."""
    
    if my_list is None:
        my_list = []  # Create a new list if none is here
    
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
