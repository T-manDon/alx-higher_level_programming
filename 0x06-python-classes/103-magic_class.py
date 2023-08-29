#!/usr/bin/python3
"""Define  matching bytecode by Holberton."""

import math

# Define the MagicClass class
class MagicClass:
    """Represent a circle."""

    # Constructor (initializer) for the MagicClass class
    def __init__(self, radius=0):
        """Initialize a MagicClass.

        Args:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        # Check if the radius is a number (int or float)
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    # Method to calculate the area of the MagicClass
    def area(self):
        """Return the areas."""
        return self.__radius ** 2 * math.pi

    # Method to calculate the circumference of the MagicClass
    def circumference(self):
        """Return The MagicClass circum."""
        return 2 * math.pi * self.__radius
