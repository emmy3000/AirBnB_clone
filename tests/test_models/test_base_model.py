#!/usr/bin/python3
"""
Unittest module for BaseModel class.
"""
import unittest
import os
from datetime import datetime
import json
import re
import time
import uuid

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
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
        Test instantiation of BaseModel class.
        """
        base_model = BaseModel()
        self.assertEqual(
            str(type(base_model)),
            "<class 'models.base_model.BaseModel'>"
        )
        self.assertIsInstance(base_model, BaseModel)
        self.assertTrue(
            issubclass(type(base_model), BaseModel)
        )

    def test_init_no_args(self):
        """
        Test __init__ method without arguments.
        """
        self.reset_storage()
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_init_many_args(self):
        """
        Test __init__ method having too many arguments.
        """
        self.reset_storage()
        args = [i for i in range(1000)]
        base_model = BaseModel(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        base_model = BaseModel(*args)

    def test_attributes(self):
        """
        Test attributes value for an instance of the BaseModel class.
        """
        attributes = storage.attributes()["BaseModel"]
        instance = BaseModel()
        for key, value in attributes.items():
            self.assertTrue(hasattr(instance, key))
            self.assertEqual(type(getattr(instance, key, None)), value)

    def test_datetime_created(self):
        """
        Test if updated_at and created_at are currently at creation phase.
        """
        date_now = datetime.now()
        base_model = BaseModel()
        diff = base_model.updated_at - base_model.created_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
        diff = base_model.created_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.1)

    def test_id(self):
        """
        Test for unique user id.
        """
        ids = [BaseModel().id for _ in range(1000)]
        self.assertEqual(len(set(ids)), len(ids))

    def test_save(self):
        """
        Test the public instance's method save().
        """
        base_model = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        base_model.save()
        diff = base_model.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_str(self):
        """
        Test the __str__ method.
        """
        base_model = BaseModel()
        rex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        result = rex.match(str(base_model))
        self.assertIsNotNone(result)
        self.assertEqual(result.group(1), "BaseModel")
        self.assertEqual(result.group(2), base_model.id)
        string = result.group(3)
        string = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", string)
        dictionary = json.loads(string.replace("'", '"'))
        instance_dict = base_model.__dict__.copy()

    def test_to_dict(self):
        """
        Test the public instance method to_dict().
        """
        base_model = BaseModel()
        base_model.name = "Betty"
        base_model.age = 28
        serialized_dict = base_model.to_dict()
        self.assertEqual(serialized_dict["id"], base_model.id)
        self.assertEqual(serialized_dict["__class__"], type(base_model).__name__)
        self.assertEqual(serialized_dict["created_at"], base_model.created_at.isoformat())
        self.assertEqual(serialized_dict["updated_at"], base_model.updated_at.isoformat())
        self.assertEqual(serialized_dict["name"], base_model.name)
        self.assertEqual(serialized_dict["age"], base_model.age)

    def test_to_dict_no_args(self):
        """
        Test to_dict() without arguments.
        """
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict()
        expected_message = "to_dict() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), expected_message)

    def test_to_dict_excess_args(self):
        """
        Test to_dict() having too many arguments.
        """
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict(self, 76)
        expected_message = "to_dict() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), expected_message)

    def test_instantiation_with_kwargs(self):
        """
        Test instantiation with **kwargs.
        """
        my_model = BaseModel()
        my_model.name = "Alchemist"
        my_model.my_number = 1337
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_new_model.to_dict(), my_model.to_dict())

    def test_instantiation_with_kwargs_dict(self):
        """
        Test instantiation with **kwargs from a custom dictionary.
        """
        custom_dict = {
            "__class__": "BaseModel",
            "updated_at": datetime(2043, 11, 25, 23, 45, 55, 123456).isoformat(),
            "created_at": datetime.now().isoformat(),
            "id": uuid.uuid4(),
            "var": "foobar",
            "int": 100,
            "float": 3.33
        }
        instance = BaseModel(**custom_dict)
        self.assertEqual(instance.to_dict(), custom_dict)

    def test_save_calls_storage_save(self):
        """
        Test to ensure that storage.save() is called from save().
        """
        self.resetStorage()
        base_model = BaseModel()
        base_model.save()
        key = "{}.{}".format(type(base_model).__name__, base_model.id)
        expected_data = {key: base_model.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path, "r", encoding="utf-8") as f:
            file_data = f.read()
            self.assertEqual(len(file_data), len(json.dumps(expected_data)))
            f.seek(0)
            self.assertEqual(json.load(f), expected_data)

    def test_save_no_args(self):
        """
        Test save() without arguments.
        """
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save()
        expected_message = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), expected_message)

    def test_save_excess_args(self):
        """
        Test save() containing too many arguments.
        """
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save(self, 98)
        expected_message = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), expected_message)

if __name__ == '__main__':
    unittest.main()
