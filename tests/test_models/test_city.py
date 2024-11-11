#!/usr/bin/python3
"""Unittest module for the City class."""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Tests the City class."""

    def test_instance_creation(self):
        """Test instantiation of City."""
        obj = City()
        self.assertIsInstance(obj, City)
        self.assertEqual(obj.state_id, "")
        self.assertEqual(obj.name, "")


if __name__ == '__main__':
    unittest.main()
