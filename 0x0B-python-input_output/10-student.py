#!/usr/bin/python3
"""10-student.py """

class Student:
    """
    Simple class.

    Args:
        first_name (str): The name of student.
        last_name (str): The family name.
        age (int): The age.

    Attributes:
        first_name (str): The name of student.
        last_name (str): The family name.
        age (int): The age.

    """
    def __init__(self, first_name, last_name, age):
        # Initialize the student's attributes when creating an instance of the class.
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary.

        Args:
            attrs (list of str): A list dictionary.

        Returns:
            dict: A dictionary.
        """
        ret_dict = {}
        if type(attrs) is list:
            # Check if `attrs` is a list of strings; otherwise, return the entire dictionary.
            for item in attrs:
                if type(item) is not str:
                    return self.__dict__
            # Populate `ret_dict` with only the specified attributes from `attrs`.
            for key in attrs:
                if key in self.__dict__:
                    ret_dict.update({key: self.__dict__[key]})
            return ret_dict
        else:
            # If `attrs` is not a list, return the entire dictionary.
            return self.__dict__
