#!/usr/bin/python3
"""Unit tests for Square class"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for the Square class"""

    def test_size(self):
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_str(self):
        s = Square(5, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_size_setter(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_type_error(self):
        s = Square(5)
        with self.assertRaises(TypeError):
            s.size = "9"

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 1)
        expected = {"id": 1, "size": 10, "x": 2, "y": 1}
        self.assertEqual(s.to_dictionary(), expected)

    def test_update_args(self):
        s = Square(5)
        s.update(10)
        self.assertEqual(s.id, 10)


if __name__ == "__main__":
    unittest.main()
