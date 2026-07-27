#!/usr/bin/python3
"""Defines a MyInt class."""


class MyInt(int):
    """Represents an integer with inverted == and != operators."""

    def __eq__(self, other):
        """Return True if self is NOT equal to other."""
        return int(self) != int(other)

    def __ne__(self, other):
        """Return True if self IS equal to other."""
        return int(self) == int(other)
