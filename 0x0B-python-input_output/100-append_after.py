#!/usr/bin/python3
"""100-append_after.py """
def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of tex.

    Args:
        filename (str): file to searc
        search_string (str): term
        new_string (str): line to insert.
    """
    with open(filename, 'r+', encoding='utf-8') as curr_file:
        lines = curr_file.readlines()
        curr_file.seek(0)
        for i, line in enumerate(lines):
            #            print("read:   {}".format(line), end='')
            if search_string in line:
                lines[i] = line + new_string
                #                print("modded: {}".format(line), end='')
#        for line in lines:
#            print(line, end="")
        curr_file.writelines(lines)
