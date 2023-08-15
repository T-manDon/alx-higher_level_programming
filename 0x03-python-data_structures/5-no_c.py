#!/usr/bin/python3

def no_c(my_string):

    """
    Remove all c and C characters.
    """

    copy = [x for x in my_string if x != 'c' and x != 'C']

    return ''.join(copy)
