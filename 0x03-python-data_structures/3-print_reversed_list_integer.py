#!/usr/bin/python3

def print_reversed_list_integer(my_list=None):
    """
    Print all integers of a list in reverse order.
    """
    if my_list is None:
        my_list = []  # Create a new list if none exists

    if isinstance(my_list, list):
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
