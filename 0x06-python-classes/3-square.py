#!/usr/bin/python3
"""create a new square instance"""

class Square:
    """represent a square"""

    def __init__(self, size=0):
        """Initializes a new square

        Args:
            size (int): The size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Find the square of size"""
        return (self.__size ** 2)
