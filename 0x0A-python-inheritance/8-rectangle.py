#!/usr/bin/python3

class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = 0  # Initialize to 0
        self.__height = 0  # Initialize to 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

# Example usage:
if __name__ == "__main__":
    try:
        r = Rectangle(5, 4)
        print(f"Width: {r.__width}, Height: {r.__height}")
        print(f"Area: {r.area()}")
    except Exception as e:
        print(e)  # Output: Width: 5, Height: 4, Area: 20

    try:
        r = Rectangle(0, 4)  # Invalid width
    except Exception as e:
        print(e)  # Output: width must be greater than 0

    try:
        r = Rectangle(5, "4")  # Invalid height
    except Exception as e:
        print(e)  # Output: height must be an integer
