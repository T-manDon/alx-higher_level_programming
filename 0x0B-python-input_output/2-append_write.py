#!/usr/bin/python3

def append_write(filename="", text=""):
    try:
        with open(filename, mode="a", encoding="utf-8") as file:
            num_characters_added = file.write(text)
        return num_characters_added
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
