#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.

    Args:
    obj: Any Python object.
    a_class: A Python class.

    Returns:
    True if obj is an instance of a_class, otherwise False.
    """
    return type(obj) is a_class

# Example usage:
if __name__ == "__main__":
    class ExampleClass:
        pass

    obj1 = ExampleClass()
    obj2 = "Hello, World!"
    
    print(is_same_class(obj1, ExampleClass))  # True
    print(is_same_class(obj2, ExampleClass))  # False
