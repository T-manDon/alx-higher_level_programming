!/usr/bin/python3
"""The int adds values add_integer(a, b).
"""
def add_integer(a, b=98):
    """
    Gives addition of a and b.

    Args:
        a (int, float): the first value.
        b (int, float): the second value.
    """
    if type(a) in [int, float]:
        try:
            a = int(a)
        except:
            raise TypeError('a must be an integer')
    else:
        raise TypeError('a must be an integer')

    if type(b) in [int, float]:
        try:
            b = int(b)
        except:
            raise TypeError('b must be an integer')
    else:
        raise TypeError('b must be an integer')

    return a + b
