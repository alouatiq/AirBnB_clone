#!/usr/bin/python3
"""Unittest module for the Place class."""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests the Place class."""

    def test_instance_creation(self):
        """Test instantiation of Place."""
        obj = Place()
        self.assertIsInstance(obj, Place)
        self.assertEqual(obj.city_id, "")
        self.assertEqual(obj.user_id, "")
        self.assertEqual(obj.name, "")
        self.assertEqual(obj.description, "")
        self.assertEqual(obj.number_rooms, 0)
        self.assertEqual(obj.number_bathrooms, 0)
        self.assertEqual(obj.max_guest, 0)
        self.assertEqual(obj.price_by_night, 0)
        self.assertEqual(obj.latitude, 0.0)
        self.assertEqual(obj.longitude, 0.0)
        self.assertEqual(obj.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()
