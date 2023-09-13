#!/usr/bin/python3
"""5-save_to_json_file.py """
def save_to_json_file(my_obj, filename):
    """Writes Object to text file.

    Args:
        my_obj (object): The serialised object.
        filename (str): The file name.
    """
    import json

    # Open the file in 'w' mode (write mode) to create or overwrite the file.
    with open(filename, 'w', encoding='utf-8') as file:
        # Use `json.dump()` to serialize the Python object and write it to the file
        # in JSON format.
        json.dump(my_obj, file)
