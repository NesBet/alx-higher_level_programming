#!/usr/bin/python3
"""
Creates a class Square with private instance attributes size and position,
and public instance methods to calculate area and print square.
"""


class Square:
    """
    Defines a class with private instance attributes size and position,
    and public instance methods to calculate area and print square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes attributes size and position.

        Args:
            size (int): The size of the square's side.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the private instance attribute size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the private instance attribute size."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Gets the private instance attribute position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the private instance attribute position."""
        if (
            type(value) is not tuple
            or len(value) != 2
            or type(value[0]) is not int
            or type(value[1]) is not int
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates and returns the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Prints a square of size self.__size using '#'."""
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for _ in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()

    def my_print_string(self):
        """Formats a returnable string like my_print."""
        square_string = ""
        if self.__size > 0:
            for y in range(self.__position[1]):
                square_string += "\n"
            for _ in range(self.__size):
                for x in range(self.__position[0]):
                    square_string += " "
                for _ in range(self.__size):
                    square_string += "#"
                if y != (self.__size - 1):
                    square_string += "\n"
        return square_string

    def __repr__(self):
        """Returns the square representation as a string."""
        return self.my_print_string()

