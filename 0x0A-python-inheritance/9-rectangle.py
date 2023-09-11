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
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        return self.__str__()

# Example usage:
if __name__ == "__main__":
    try:
        r = Rectangle(5, 4)
        print(r)  # Output: [Rectangle] 5/4
        print(f"Area: {r.area()}")  # Output: Area: 20
    except Exception as e:
        print(e)

    try:
        r = Rectangle(0, 4)  # Invalid width
    except Exception as e:
        print(e)  # Output: width must be greater than 0

    try:
        r = Rectangle(5, "4")  # Invalid height
    except Exception as e:
        print(e)  # Output: height must be an integer
