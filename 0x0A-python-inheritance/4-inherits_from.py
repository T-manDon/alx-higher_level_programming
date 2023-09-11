#!/usr/bin/python3

def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherits (directly or indirectly)
    from the specified class.

    Args:
    obj: Any Python object.
    a_class: A Python class.

    Returns:
    True if obj is an instance of a class that inherits from a_class, otherwise False.
    """
    # Base case: if obj is an instance of a_class, return True
    if isinstance(obj, a_class):
        return True
    
    # Get the classes that obj inherits from directly
    obj_base_classes = obj.__class__.__bases__

    # Recursively check if any base class inherits from a_class
    for base_class in obj_base_classes:
        if inherits_from(base_class, a_class):
            return True
    
    return False

# Example usage:
if __name__ == "__main__":
    class Grandparent:
        pass

    class Parent(Grandparent):
        pass

    class Child(Parent):
        pass

    obj1 = Child()
    obj2 = Parent()
    obj3 = "Hello, World!"

    print(inherits_from(obj1, Grandparent))  # True (Child inherits from Grandparent indirectly)
    print(inherits_from(obj2, Child))  # False (Parent does not inherit from Child)
    print(inherits_from(obj3, str))  # True (obj3 is an instance of str)
