#!/usr/bin/python3
"""9-student.py """

class Student:
    """Simple class with student data.

    Args:
        first_name (str): The first name
        last_name (str): The family name
        age (int): The student age

    Attributes:
        first_name (str): The  name.
        last_name (str): Surname.
        age (int): The age of the student.

    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary.

        Returns:
            dict: A dictionary.
        """
        # Use the `__dict__` attribute of the object to retrieve its attributes as a dictionary.
        return self.__dict__
