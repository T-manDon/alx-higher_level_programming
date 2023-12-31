#!/usr/bin/python3
"""
Rectangle Class: Defines a Rectangle
"""
class Rectangle:
    """ A class for defining rectangles with attributes and public methods """
    def __init__(self, width=0, height=0):
        """ Initializes instances of rectangles """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Get the width of the rectangle """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Set the width of the rectangle """
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Get the height of the rectangle """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Set the height of the rectangle """
        if not (isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calculate and return the area of the rectangle """
        return (self.__height * self.__width)

    def perimeter(self):
        """ Calculate and return the perimeter of the rectangle """
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return (2 * (self.__width + self.__height))
