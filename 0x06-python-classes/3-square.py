#!/usr/bin/python3
"""Define a class Square."""

# Define the Square class
class Square:
    """Represent a square."""

    # Constructor (initializer) for the Square class
    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        # Check if the size is an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        # Check if the size is non-negative
        elif size < 0:
            raise ValueError("size must be >= 0")
        
        # Store the size in a private attribute "__size"
        self.__size = size

    # Method to calculate the area of the square
    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size
