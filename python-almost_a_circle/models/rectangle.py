import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_initialization(self):
        r = Rectangle(10, 5, 1, 1, 42)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 42)

    def test_area(self):
        r = Rectangle(4, 6)
        self.assertEqual(r.area(), 24)
