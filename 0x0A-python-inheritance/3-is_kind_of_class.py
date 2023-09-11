#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if it inherits from, the specified class.

    Args:
    obj: Any Python object.
    a_class: A Python class.

    Returns:
    True if obj is an instance of a_class or inherits from it, otherwise False.
    """
    return isinstance(obj, a_class)

# Example usage:
if __name__ == "__main__":
    class ParentClass:
        pass

    class ChildClass(ParentClass):
        pass

    obj1 = ChildClass()
    obj2 = ParentClass()
    obj3 = "Hello, World!"
    
    print(is_kind_of_class(obj1, ParentClass))  # True (obj1 is an instance of ChildClass, which inherits from ParentClass)
    print(is_kind_of_class(obj2, ChildClass))  # False (obj2 is an instance of ParentClass, not ChildClass)
    print(is_kind_of_class(obj3, str))  # True (obj3 is an instance of str)
