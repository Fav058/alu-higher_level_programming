#!/usr/bin/python3
"""Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square, inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Returns the string representation of the Square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
