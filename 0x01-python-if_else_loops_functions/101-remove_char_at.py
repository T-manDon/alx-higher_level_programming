#!/usr/bin/python3
# 101-rmove_cha-t.py

def remove_char_at(str, n):

    """
    Create a string copy n.
    """

    if n < 0:

        return (str)

    return (str[:n] + str[n+1:])
