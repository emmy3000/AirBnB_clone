#!/usr/bin/python3
"""
Unit test module for the FileStorage class.
"""
import unittest
from datetime import datetime
import json
from time import sleep

from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class without the setUp or tearDown
    method definitions since shared resources and dependencies
    that would need to be initialized are absent.
    """

    def test_instantiation(self):
        """
        Test instantiation of FileStorage class.
        """
        file_storage = FileStorage()
        self.assertIsInstance(file_storage, FileStorage)

    def test_docs(self):
        """
        Test docstrings of FileStorage class' methods.
        """
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)


if __name__ == '__main__':
    unittest.main()
