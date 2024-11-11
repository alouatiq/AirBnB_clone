#!/usr/bin/python3
"""Unittest module for the BaseModel class."""
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """Tests the BaseModel class."""

    def test_instance_creation(self):
        """Test instantiation of BaseModel."""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime.datetime)
        self.assertIsInstance(obj.updated_at, datetime.datetime)

    def test_str_representation(self):
        """Test __str__ method."""
        obj = BaseModel()
        string = f"[BaseModel] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), string)

    def test_save_method(self):
        """Test save method updates updated_at."""
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, old_updated_at)

    def test_to_dict_method(self):
        """Test to_dict method returns a dictionary."""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertIsInstance(obj_dict["created_at"], str)
        self.assertIsInstance(obj_dict["updated_at"], str)


if __name__ == '__main__':
    unittest.main()
