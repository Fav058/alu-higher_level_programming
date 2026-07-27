#!/usr/bin/python3
"""Defines a MyList class."""


class MyList(list):
    """Represents a list with a sorted-print capability."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
