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
        self.size = size

    # Getter method for the "size" property
    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    # Setter method for the "size" property
    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size value.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    # Method to calculate the area of the square
    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    # Define the == comparison for a Square
    def __eq__(self, other):
        """Define the == comparison for a Square.

        Args:
            other (Square): The other Square to compare with.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    # Define the != comparison for a Square
    def __ne__(self, other):
        """Define the != comparison for a Square.

        Args:
            other (Square): The other Square to compare with.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    # Define the < comparison for a Square
    def __lt__(self, other):
        """Define the < comparison for a Square.

        Args:
            other (Square): The other Square to compare with.

        Returns:
            bool: True if the area is less, False otherwise.
        """
        return self.area() < other.area()

    # Define the <= comparison for a Square
    def __le__(self, other):
        """Define the <= comparison for a Square.

        Args:
            other (Square): The other Square to compare with.

        Returns:
            bool: True if the area is less or equal, False otherwise.
        """
        return self.area() <= other.area()

    # Define the > comparison for a Square
    def __gt__(self, other):
        """Define the > comparison for a Square.

        Args:
            other (Square): The other Square to compare with.

        Returns:
            bool: True if the area is greater, False otherwise.
        """
        return self.area() > other.area()

    # Define the >= comparison for a Square
    def __ge__(self, other):
        """Define the >= comparison for a Square.

        Args:
            other (Square): The other Square to compare with.

        Returns:
            bool: True if the area is greater or equal, False otherwise.
        """
        return self.area() >= other.area()
