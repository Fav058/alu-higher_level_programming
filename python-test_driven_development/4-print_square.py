#!/usr/bin/python3
"""Module that prints a square made of the character #.
"""


def print_square(size):
    """Print a square of the given size using the # character.
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
