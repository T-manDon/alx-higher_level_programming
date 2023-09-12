#!/usr/bin/python3

"""
Rectangle inherits from BaseGeometry
"""
# Import the BaseGeometry class from module 7-base_geometry
BaseGeometry = __import__('7-base_geometry').BaseGeometry

# Define a new class called Rectangle that inherits from BaseGeometry
class Rectangle(BaseGeometry):
    """
    Rectangle data inherits from BaseGeometry
    """

    # Initialize the Rectangle object with width and height parameters
    def __init__(self, width, height):
        # Call the integer_validator method from the BaseGeometry class
        # to validate that 'width' is a positive integer
        super().integer_validator("width", width)
        
        # Call the integer_validator method from the BaseGeometry class
        # to validate that 'height' is a positive integer
        super().integer_validator("height", height)
        
        # Initialize private instance variables __width and __height with
        # the values passed as arguments
        self.__width = width
        self.__height = height

    # Define a method 'area' to calculate the area of the rectangle
    def area(self):
        """
        Method that calculates the area of the rectangle
        """
        return self.__width * self.__height

    # Define the __str__ method to provide a string representation of the rectangle
    def __str__(self):
        """
        Magic method to return the rectangle description
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
