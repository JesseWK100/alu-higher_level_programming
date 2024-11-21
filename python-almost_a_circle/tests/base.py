import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id_assignment(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)

    def test_to_json_string(self):
        data = [{"id": 1, "name": "Rectangle"}]
        json_data = Base.to_json_string(data)
        self.assertEqual(json_data, '[{"id": 1, "name": "Rectangle"}]')
