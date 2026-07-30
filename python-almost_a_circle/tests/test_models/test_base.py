#!/usr/bin/python3
"""Unit tests for Base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for the Base class"""

    def test_id_assigned(self):
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_auto_increment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string(self):
        d = [{"id": 1}]
        self.assertEqual(Base.to_json_string(d), '[{"id": 1}]')

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string(self):
        s = '[{"id": 1}]'
        self.assertEqual(Base.from_json_string(s), [{"id": 1}])


if __name__ == "__main__":
    unittest.main()
