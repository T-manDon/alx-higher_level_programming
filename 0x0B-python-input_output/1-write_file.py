#!/usr/bin/python3
"""write_file.py """

def write_file(filename="", text=""):
    """
    Write a string to a text file and return

    Args:
        filename (str): The file nam.
        text (str): The string of character.

    Returns:
        int: The number of characters written.
    """
    # Open the file with 'w' flag to ensure existing content is replaced.
    with open(filename, 'w', encoding='utf-8') as file:
        chars_written = file.write(text)
        return chars_written
