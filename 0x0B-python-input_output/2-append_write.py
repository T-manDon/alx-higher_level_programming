#!/usr/bin/python3
def append_write(filename: str = "", text: str = "") -> int:
    """
    Appends a string to the text end

    Args:
        filename (str): file name.
        text (str): The string of characters.

    Returns:
        int: The number appended.
    """
    # Open the file in 'a' mode (append mode) to add text at the end.
    # Use 'utf-8' encoding to handle text in UTF-8 format.
    with open(filename, 'a', encoding='utf-8') as file:
        # Write the provided text to the file and capture the count
        # of characters written.
        chars_written = file.write(text)
        return chars_written
