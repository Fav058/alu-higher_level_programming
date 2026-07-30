#!/usr/bin/python3
"""Unit tests for Rectangle class"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class"""

    def test_width_height(self):
        r = Rectangle(3, 5)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 5)

    def test_default_x_y(self):
        r = Rectangle(3, 5)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_width_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle("3", 5)

    def test_width_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(-3, 5)

    def test_x_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 5, {})

    def test_y_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(3, 5, 0, -1)

    def test_area(self):
        r = Rectangle(3, 5)
        self.assertEqual(r.area(), 15)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 1)
        expected = {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(r.to_dictionary(), expected)

    def test_update_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(r.height, 1)


if __name__ == "__main__":
    unittest.main()
