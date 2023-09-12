#!/usr/bin/python3
"""
inherits_from
"""
def inherits_from(obj, a_class):
    """
    Function that returns True if object inst, otherwise false
    """
    if type(obj) is a_class or not isinstance(obj, a_class):
        return False
    else:
        return True
