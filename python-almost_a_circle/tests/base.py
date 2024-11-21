#!/usr/bin/python3
"""Unittest for Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Defines tests for the Base class."""

    def setUp(self):
        """Reset the __nb_objects counter before each test."""
        Base._Base__nb_objects = 0

    def test_auto_id_increment(self):
        """Test auto-increment behavior of the id attribute."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_custom_id(self):
        """Test assigning a custom id."""
        b = Base(100)
        self.assertEqual(b.id, 100)

    def test_mixed_auto_and_custom_id(self):
        """Test mixed auto-increment and custom id behavior."""
        b1 = Base()
        b2 = Base(200)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 200)
        self.assertEqual(b3.id, 2)

    def test_private_attribute_access(self):
        """Test that __nb_objects is not directly accessible."""
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)


if __name__ == "__main__":
    unittest.main()

