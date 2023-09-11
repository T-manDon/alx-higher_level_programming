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

# Example usage:
if __name__ == "__main__":
    # Creating an instance of the BaseGeometry class
    geometry = BaseGeometry()
    
    # Calling the area() method will raise an exception
    try:
        geometry.area()
    except Exception as e:
        print(e)  # Output: area() is not implemented
