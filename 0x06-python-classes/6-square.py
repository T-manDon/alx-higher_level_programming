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
        # Initialize the size and position using the property setters
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
        # Check if the new size value is an integer
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        # Check if the new size value is non-negative
        elif value < 0:
            raise ValueError("size must be >= 0")
        
        # Set the new size value to the private attribute "__size"
        self.__size = value

    # Getter method for the "position" property
    @property
    def position(self):
        """Get/set the current position of the square."""
        return self.__position

    # Setter method for the "position" property
    @position.setter
    def position(self, value):
        # Check if the new position value is a valid tuple
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        
        # Set the new position value to the private attribute "__position"
        self.__position = value

    # Method to calculate the area of the square
    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    # Method to print the square with position and "#" characters
    def my_print(self):
        """Print the square with the # character."""
        # If the size is 0, print an empty line
        if self.__size == 0:
            print("")
            return

        # Print empty lines for the vertical position
        [print("") for i in range(0, self.__position[1])]
        
        # Print each row of the square with position and "#" characters
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
