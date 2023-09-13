#!/usr/bin/python3
"""8-class_to_json.py """

def class_to_json(obj):
    """Returns a dictionary description.
    Args:
        obj (any): The object.

    Returns:
        dict: A dictionary.
    """
    # Use the `__dict__` attribute of the object to retrieve its attributes as a dictionary.
    return obj.__dict__
