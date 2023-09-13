#!/usr/bin/python3
"""7-add_item.py """

# Import the 'argv' variable from the 'sys' module to access command-line arguments.
from sys import argv

# Import the 'save_to_json_file' and 'load_from_json_file' functions from their respective modules.
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
