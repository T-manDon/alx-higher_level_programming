#!/usr/bin/python3

"""
Square inherits from BaseGeometry
"""
# Import the Rectangle class from module 9-rectangle
Rectangle = __import__('9-rectangle').Rectangle

# Define a new class called Square that inherits from Rectangle
class Square(Rectangle):
    """
    Square data that inherits from Rectangle
    """

    # Initialize the Square object with a 'size' parameter
    def __init__(self, size):
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
        calculate the area
        """
        return self.__size * self.__size
