#!/usr/bin/python3
"""Define a class Square."""

# Define the Square class
class Square:
    """Represent a square."""

    # Constructor (initializer) for the Square class
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

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

    # Getter method for the "position" property
    @property
    def position(self):
        """Get/set the current position of the square."""
        return self.__position

    # Setter method for the "position" property
    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The new position value as a tuple (int, int).
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    # Method to calculate the area of the square
    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    # Method to print the square with position and "#" characters
    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    # Custom string representation of the Square
    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ""
