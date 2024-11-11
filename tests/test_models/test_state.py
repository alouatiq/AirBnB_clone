#!/usr/bin/python3
"""Unittest module for the State class."""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Tests the State class."""

    def test_instance_creation(self):
        """Test instantiation of State."""
        obj = State()
        self.assertIsInstance(obj, State)
        self.assertEqual(obj.name, "")


if __name__ == '__main__':
    unittest.main()
