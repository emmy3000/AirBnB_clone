#!/usr/bin/python3
"""
Unittest module for the City class.
"""
import unittest
import os
from datetime import datetime
import time
import re
import json

from models.city import City
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    Test cases for the City class.
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
        Test instantiation of City class.
        """
        city = City()
        self.assertEqual(
            str(type(city)),
            "<class 'models.city.City'>"
        )
        self.assertIsInstance(city, City)
        self.assertTrue(
            issubclass(type(city), BaseModel)
        )

    def test_attributes(self):
        """
        Test attributes of the City class.
        """
        attributes = storage.attributes()["City"]
        city = City()
        for attr_name, attr_type in attributes.items():
            self.assertTrue(hasattr(city, attr_name))
            self.assertEqual(type(
                getattr(city, attr_name, None)
            ), attr_type)


if __name__ == "__main__":
    unittest.main()  # !/usr/bin/python3
"""
Unittest module for the City class.
"""


class TestCity(unittest.TestCase):
    """
    Test cases for the City class.
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
        Test instantiation of City class.
        """
        city = City()
        self.assertEqual(
            str(type(city)),
            "<class 'models.city.City'>"
        )
        self.assertIsInstance(city, City)
        self.assertTrue(
            issubclass(type(city), BaseModel)
        )

    def test_attributes(self):
        """
        Test attributes of the City class.
        """
        attributes = storage.attributes()["City"]
        city = City()
        for attr_name, attr_type in attributes.items():
            self.assertTrue(hasattr(city, attr_name))
            self.assertEqual(type(
                getattr(city, attr_name, None)
            ), attr_type)


if __name__ == "__main__":
    unittest.main()
