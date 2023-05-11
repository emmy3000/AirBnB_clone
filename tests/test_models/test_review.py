#!/usr/bin/python3
"""
Unittest module for the Review class.
"""

import unittest
import os
from datetime import datetime
import time
import re
import json

from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """
    Test cases for the Review class.
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
        Test instantiation of Review class.
        """
        review = Review()
        self.assertEqual(
            str(type(review)),
            "<class 'models.review.Review'>"
        )
        self.assertIsInstance(review, Review)
        self.assertTrue(
            issubclass(type(review), BaseModel)
        )

    def test_attributes(self):
        """
        Test attributes of the Review class.
        """
        attributes = storage.attributes()["Review"]
        review = Review()
        for attr_name, attr_type in attributes.items():
            self.assertTrue(hasattr(review, attr_name))
            self.assertEqual(type(getattr(
                review, attr_name, None
            )), attr_type)


if __name__ == "__main__":
    unittest.main()
