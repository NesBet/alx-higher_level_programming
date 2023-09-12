#!/usr/bin/python3
"""Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square representation."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size: Size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
