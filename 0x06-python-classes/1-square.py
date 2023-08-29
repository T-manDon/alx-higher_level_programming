#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """Represent a square.

    This class defines a square with a private size attribute.
    """

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
