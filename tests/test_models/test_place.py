
#!/usr/bin/python3
"""
Unittest module for the Place class.
"""
import unittest
import os
from datetime import datetime
import time
import re
import json

from models.place import Place
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """
    Test cases for the Place class.
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
        Test instantiation of Place class.
        """
        place = Place()
        self.assertEqual(
            str(type(place)),
            "<class 'models.place.Place'>"
        )
        self.assertIsInstance(place, Place)
        self.assertTrue(
            issubclass(type(place), BaseModel)
        )

    def test_attributes(self):
        """
        Test attributes of the Place class.
        """
        attributes = storage.attributes()["Place"]
        place = Place()
        for attr_name, attr_type in attributes.items():
            self.assertTrue(hasattr(place, attr_name))
            self.assertEqual(type(
                getattr(place, attr_name, None)
            ), attr_type)


if __name__ == "__main__":
    unittest.main()
