#!/usr/bin/python3
"""3-to_json_string.py """
def to_json_string(my_obj):
    """
    Returns the serialized string

    Args:
        my_obj (any): serialized objects

    """
    import json

    return json.dumps(my_obj)
