#!/usr/bin/python3
"""
Unittest module for the User class.
"""
import unittest
import os
from datetime import datetime
import time
import re
import json

from models.user import User
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    Test cases for the User class.
    """

    def setUp(self):
        """
        Set up test environment.
        """
        pass

    def tearDown(self):
        """
        Tear down test environment.
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
        Test instantiation of User class.
        """
        user = User()
        self.assertEqual(
            str(type(user)),
            "<class 'models.user.User'>"
        )
        self.assertIsInstance(user, User)
        self.assertTrue(
            issubclass(type(user), BaseModel)
        )

    def test_attributes(self):
        """
        Test attributes of the User class.
        """
        attributes = storage.attributes()["User"]
        user = User()
        for attr_name, attr_type in attributes.items():
            self.assertTrue(hasattr(user, attr_name))
            self.assertEqual(type(
                getattr(user,
                        attr_name,
                        None)
            ), attr_type)


if __name__ == "__main__":
    unittest.main()
