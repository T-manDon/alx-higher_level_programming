#!/usr/bin/python3

def read_file(filename=""):
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            contents = file.read()
            print(contents, end="")  # Print the file contents to stdout
    except FileNotFoundError:
        pass  # Do nothing if the file doesn't exist
