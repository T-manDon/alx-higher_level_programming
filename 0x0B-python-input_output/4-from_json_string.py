#!/usr/bin/python3
""" 4-from_json_string.py """

def from_json_string(my_str):
    """
    Returns an object

    Args:
        my_str (str): A JSON string serialized object.

    Returns:
        obj: The Python object deserialized.
    """
    import json

    # Use the `json.loads()` method to parse the JSON string and
    # convert it back into a Python object.
    return json.loads(my_str)
