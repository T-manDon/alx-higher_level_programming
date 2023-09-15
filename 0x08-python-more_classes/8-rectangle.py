#!/usr/bin/python3
"""
Rectangle Class: Definition of a Rectangle
"""


class Rectangle:
    """A class that defines a Rectangle with attributes and public methods"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Constructor: Initializes instances of rectangles.

        Args:
            width (int): Width of the rectangle. Default is 0.
            height (int): Height of the rectangle. Default is 0.
        """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method that returns the bigger or equal rectangle
        based on the area.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Returns:
            Rectangle: The rectangle with the larger or equal area.
        
        Raises:
            TypeError: If either rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not (isinstance(rect_1, Rectangle)) or not (isinstance(rect_2, Rectangle)):
            raise TypeError("Both rect_1 and rect_2 must be instances of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @property
    def width(self):
        """Retrieve the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): Width value to be set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): Height value to be set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not (isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Magic method that prints the rectangle with the specified character.

        Returns:
            str: A string representation of the rectangle.
        """
        string = ""
        if self.__width != 0 and self.__height != 0:
            for x in range(self.__height):
                for y in range(self.__width):
                    string += str(self.print_symbol)
                string += "\n"
            string = string[:-1]
        return string

    def __repr__(self):
        """
        Return a string representation of the rectangle for recreation.

        Returns:
            str: A string representation that can recreate a new instance.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Destructor: Detect when an instance of Rectangle is deleted
        and print a message.
        """
        # Decrement the number of instances when an instance is deleted
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
