#!/usr/bin/python3
"""11-student.py """

class Student:
    """
    Simple class containing student data.

    Args:
        first_name (str): The name of student.
        last_name (str): The family name.
        age (int): The age.

    Attributes:
        first_name (str): The given name.
        last_name (str): The family name.
        age (int): The age.

    """
    def __init__(self, first_name, last_name, age):
        # Initialize the student's attributes when creating an instance of the class.
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation.

        Args:
            attrs (list of str): A list of keys in dictionary.

        Returns:
            dict: A dictionary containing keys.
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

    def reload_from_json(self, json):
        """
        Updates all attributes of self.
        Args:
            json (dict): A dictionary.
        """
        # Loop through the keys in the provided JSON dictionary and update the corresponding attributes.
        for key in json:
            self.__dict__.update({key: json[key]})
