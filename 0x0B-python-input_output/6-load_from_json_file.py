#!/usr/bin/python3
"""6-load_from_json_file.py """

def load_from_json_file(filename):
    """Creates JSON file.

    Args:
        filename (str): The name of the JSON fil.

    Returns:
        obj: The dicentralised the JSON file.
    """
    import json

    # Open the JSON file in 'r' mode (read mode) to read its content.
    with open(filename, encoding='utf-8') as file:
        # Use `json.load()` to parse the JSON content from the file and create
        # a Python object.
        return json.load(file)
