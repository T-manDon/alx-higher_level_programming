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

class Square(Rectangle):
    def __init__(self, size):
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        # Call the parent class (Rectangle) constructor with size as both width and height
        super().__init__(size, size)

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"

    def __repr__(self):
        return self.__str__()

# Example usage:
if __name__ == "__main__":
    try:
        s = Square(5)
        print(s)  # Output: [Square] 5/5
        print(f"Area: {s.area()}")  # Output: Area: 25
    except Exception as e:
        print(e)

    try:
        s = Square(0)  # Invalid size
    except Exception as e:
        print(e)  # Output: size must be greater than 0

    try:
        s = Square("4")  # Invalid size
    except Exception as e:
        print(e)  # Output: size must be an integer
