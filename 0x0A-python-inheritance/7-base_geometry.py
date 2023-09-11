#!/usr/bin/python3

class BaseGeometry:
    """
    Base class for geometry-related operations.
    """

    def area(self):
        """
        Raises an Exception with the message "area() is not implemented."
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value as an integer and checks if it's greater than 0.

        Args:
        name: A string representing the name of the value.
        value: The value to be validated.

        Raises:
        - TypeError if value is not an integer.
        - ValueError if value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

# Example usage:
if __name__ == "__main__":
    # Creating an instance of the BaseGeometry class
    geometry = BaseGeometry()
    
    try:
        geometry.area()
    except Exception as e:
        print(e)  # Output: area() is not implemented
    
    try:
        geometry.integer_validator("side_length", 5)
    except Exception as e:
        print(e)  # No exception is raised for a valid value
        
    try:
        geometry.integer_validator("side_length", "invalid")
    except Exception as e:
        print(e)  # Output: side_length must be an integer
    
    try:
        geometry.integer_validator("side_length", 0)
    except Exception as e:
        print(e)  # Output: side_length must be greater than 0
