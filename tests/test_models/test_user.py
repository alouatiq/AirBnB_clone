#!/usr/bin/python3
"""Unittest module for the User class."""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Tests the User class."""

    def test_instance_creation(self):
        """Test instantiation of User."""
        obj = User()
        self.assertIsInstance(obj, User)
        self.assertEqual(obj.email, "")
        self.assertEqual(obj.password, "")
        self.assertEqual(obj.first_name, "")
        self.assertEqual(obj.last_name, "")


if __name__ == '__main__':
    unittest.main()
