#!/usr/bin/python3
"""Defines a Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, inheriting from Rectangle."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size (width and height) of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not greater than 0.
        """
        super().__init__(size, size)
