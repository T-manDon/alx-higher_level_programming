#!/usr/bin/python3

"""
Square inherits from Rectanglar
"""
# Import the Rectangle class from module 9-rectangle
Rectangle = __import__('9-rectangle').Rectangle

# Define a new class called Square that inherits from Rectangle
class Square(Rectangle):
    """
    Square class inheriting from Rectangle
    """

    # Initialize the Square object with a 'size' parameter
    def __init__(self, size):
        """
        Initialize a Square object
        Args:
            size (int): The size of the square.
        """
        # Call the integer_validator method from the Rectangle class
        # to validate that 'size' is a positive integer
        super().integer_validator("size", size)
        
        # Call the constructor of the Rectangle class, passing 'size' as both
        # the width and height to represent a square
        super().__init__(size, size)
        
        # Initialize a private instance variable __size with the 'size' value
        self.__size = size

    # Define a method 'area' to calculate the area of the square
    def area(self):
        """
        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    # Define the __str__ method to provide a string representation of the square
    def __str__(self):
        """
        Returns:
            str: A string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
