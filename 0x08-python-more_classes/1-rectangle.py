#!/usr/bin/python3
"""Rectangle class"""

class Rectangle:
    """
    Defines rectangle attributes
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrieve rectangle width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ set private attribue
        """
        if not (isinstance(value, int)):
            raise TypeError("width is integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieve the rectangle height
        """
        return (self.__height)
    @height.setter
    def height(self, value):
        """ set passed private attribute of height
        """
        if not (isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
