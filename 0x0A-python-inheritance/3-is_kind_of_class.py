#!/usr/bin/python3
"""
kind class
"""
def is_kind_of_class(obj, a_class):
    """
    Returns True or false
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
