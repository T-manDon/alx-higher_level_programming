#!/usr/bin/python3
"""Define a class Square."""

# Define the Square class
class Square:
    """Represent a square."""

    # Constructor (initializer) for the Square class
    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        # Initialize the size using the property setter
        self.size = size

    # Getter method for the "size" property
    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    # Setter method for the "size" property
    @size.setter
    def size(self, value):
        # Check if the new size value is an integer
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        # Check if the new size value is non-negative
        elif value < 0:
            raise ValueError("size must be >= 0")
        
        # Set the new size value to the private attribute "__size"
        self.__size = value

    # Method to calculate the area of the square
    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    # Method to print the square using "#" characters
    def my_print(self):
        """Print the square with the # character."""
        for i in range(0, self.__size):
            # Print "#" repeatedly for each row
            [print("#", end="") for j in range(self.__size)]
            print("")  # Move to the next line after printing a row
        
        # If the size is 0, print an empty line
        if self.__size == 0:
            print("")
