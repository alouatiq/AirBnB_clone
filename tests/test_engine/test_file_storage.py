#!/usr/bin/python3
"""Unittest module for the FileStorage class."""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    """Tests the FileStorage class."""

    def setUp(self):
        """Set up test methods."""
        self.storage = FileStorage()
        self.obj = BaseModel()
        self.storage.new(self.obj)

    def tearDown(self):
        """Tear down test methods."""
        del self.obj
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all_method(self):
        """Test all method."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_method(self):
        """Test new method."""
        key = f"{self.obj.__class__.__name__}.{self.obj.id}"
        self.assertIn(key, self.storage.all())

    def test_save_method(self):
        """Test save method."""
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload_method(self):
        """Test reload method."""
        self.storage.save()
        self.storage.reload()
        key = f"{self.obj.__class__.__name__}.{self.obj.id}"
        self.assertIn(key, self.storage.all())


if __name__ == '__main__':
    unittest.main()
