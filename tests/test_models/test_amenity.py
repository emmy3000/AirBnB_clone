#!/usr/bin/python3
"""
Unittest module for the Amenity class.
"""
import unittest
import os
from datetime import datetime
import time
import re
import json

from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """

    def setUp(self):
        """
        Set up test methods.
        """
        pass

    def tearDown(self):
        """
        Tear down test methods.
        """
        self.reset_storage()

    def reset_storage(self):
        """
        Reset FileStorage data.
        """
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """
        Test instantiation of Amenity class.
        """
        amenity = Amenity()
        self.assertEqual(
            str(type(amenity)),
            "<class 'models.amenity.Amenity'>"
        )
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(
            issubclass(type(amenity), BaseModel)
        )

    def test_attributes(self):
        """
        Test attributes of the Amenity class.
        """
        attributes = storage.attributes()["Amenity"]
        amenity = Amenity()
        for attr_name, attr_type in attributes.items():
            self.assertTrue(
                hasattr(amenity, attr_name)
            )
            self.assertEqual(type(
                getattr(amenity, attr_name, None)
            ), attr_type)


if __name__ == "__main__":
    unittest.main()
