#!/usr/bin/python3
"""
Creates a class Square with a private instance attribute size
and a public instance method.
"""


class Square:
    """
    Defines a class with an instantiated and validated private instance attribute
    and a public instance method.
    """

    def __init__(self, size=0):
        """
        Initializes the instance attribute size after validation.

        Args:
            size (int): The size of the square's side.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size * self.__size

