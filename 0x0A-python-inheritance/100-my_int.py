#!/usr/bin/python3
"""
MyInt inheritance
"""
class MyInt(int):
    """
    Inherits int
    """
    def __eq__(self, value):
        """
        Magic method equals
        """
        return super().__ne__(value)
    def __ne__(self, value):
        """
        Magic method not equals
        """
        return super().__eq__(value)
