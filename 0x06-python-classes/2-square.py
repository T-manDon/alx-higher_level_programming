#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")  # Check if size is an integer
        elif size < 0:
            raise ValueError("size must be >= 0")  # Check if size is non-negative
        self.__size = size  # Set the size of the square
