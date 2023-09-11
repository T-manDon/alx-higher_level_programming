#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
    obj: Any Python object.

    Returns:
    A list of strings representing the attributes and methods of the object.
    """
    return dir(obj)

# Example usage:
if __name__ == "__main__":
    sample_list = [1, 2, 3]
    print(lookup(sample_list))
