#!/usr/bin/python3
"""Define a class square"""

class Square:
    """Represent a square"""
    def __init__(self, size=0):
        """intitialize a new square.

        Args:
            size (int): The size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be an integer")
        else:
            self.__size = size
