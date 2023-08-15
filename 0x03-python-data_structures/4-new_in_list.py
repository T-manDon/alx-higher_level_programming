#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    To replace an element in a copied list.
    """

    if idx < 0 or idx > len(my_list) - 1:
        raise IndexError("Index out of bounds")

    copy = [x for x in my_list]
    copy[idx] = element

    return copy
