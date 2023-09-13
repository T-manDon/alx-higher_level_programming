#!/usr/bin/python3
"""
Input-Output
"""
def read_file(filename=""):
    """
    Reads text contents
    Args:
        filename (str): name of fil
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
