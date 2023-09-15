#!/usr/bin/python3
"""
Rectangle Class: Defines a Rectangle
"""


class Rectangle:
    """ A class that defines a Rectangle with attributes and public methods """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Constructor: Initializes instances of rectangles """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ Retrieve the width of the rectangle """
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
        """ Retrieve the height of the rectangle """
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
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """ Magic method that prints the rectangle with the character '#' """
        string = ""
        if (self.__width != 0 and self.__height != 0):
            for x in range(self.__height):
                for y in range(self.__width):
                    string += "#"
                string += "\n"
            string = string[:-1]
        return (string)

    def __repr__(self):
        """ Return a string representation of the rectangle for recreation """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Destructor: Detect when an instance of Rectangle is deleted
        and print a message """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
