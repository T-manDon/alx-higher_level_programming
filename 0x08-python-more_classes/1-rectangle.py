#!/usr/bin/python3
"""Defines the class."""
class Rectangle:
    """Represent the rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize new rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width  # Initialize the width attribute with the provided value.
        self.height = height  # Initialize the height attribute with the provided value.

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width  # Return the private __width attribute.

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The new width value to be set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")  # Raise a TypeError if value is not an integer.
        if value < 0:
            raise ValueError("width must be >= 0")  # Raise a ValueError if value is less than 0.
        self.__width = value  # Set the private __width attribute to the provided value.

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height  # Return the private __height attribute.

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The new height value to be set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")  # Raise a TypeError if value is not an integer.
        if value < 0:
            raise ValueError("height must be >= 0")  # Raise a ValueError if value is less than 0.
        self.__height = value  # Set the private __height attribute to the provided value.
