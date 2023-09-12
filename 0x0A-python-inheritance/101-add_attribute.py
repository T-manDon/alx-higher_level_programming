#!/usr/bin/python3

"""Function add_attribute

This script defines a function 'add_attribute' that adds a new attribute
to an object if it's possible.
"""

def add_attribute(a_class, name, value):
    """Adds a new attribute to an object if it's possible.

    Args:
        a_class (object): The object to which the attribute will be added.
        name (str): The name of the attribute to be added.
        value (any): The value of the attribute.

    Raises:
        TypeError: If the object belongs to certain types (e.g., int, str, float),
                   a new attribute cannot be added.

    """
    # Set of types for which adding attributes is not allowed (membership test is O(1))
    cannot_add = {int, str, float, list, dict, tuple, frozenset, type, object}

    # Check if the type of 'a_class' is in the set of disallowed types
    if type(a_class) in cannot_add:
        raise TypeError("can't add a new attribute")

    # Add the attribute with the specified name and value to 'a_class'
    a_class.__setattr__(name, value)
