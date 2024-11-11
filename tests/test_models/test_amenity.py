#!/usr/bin/python3
"""Unittest module for the Amenity class."""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests the Amenity class."""

    def test_instance_creation(self):
        """Test instantiation of Amenity."""
        obj = Amenity()
        self.assertIsInstance(obj, Amenity)
        self.assertEqual(obj.name, "")


if __name__ == '__main__':
    unittest.main()
