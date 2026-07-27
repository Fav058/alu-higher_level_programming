#!/usr/bin/python3
"""Unittests for max_integer."""

import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty(self):
        self.assertIsNone(max_integer([]))

    def test_one(self):
        self.assertEqual(max_integer([5]), 5)

    def test_positive(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative(self):
        self.assertEqual(max_integer([-4, -2, -8]), -2)

    def test_mixed(self):
        self.assertEqual(max_integer([-3, 0, 5, 1]), 5)

    def test_duplicate(self):
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_sorted(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_reverse(self):
        self.assertEqual(max_integer([5, 4, 3]), 5)

    def test_float(self):
        self.assertEqual(max_integer([1.1, 2.2, 0.5]), 2.2)


if __name__ == "__main__":
    unittest.main()
