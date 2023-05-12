#!/usr/bin/python3

import json


class FileStorage:
    """
    A class that serializes instances to a JSON file and deserializes JSON
    file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets the obj in __objects with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file.
        """
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as obj_file:
            json.dump(obj_dict, obj_file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (if it exists).
        """
        try:
            with open(self.__file_path, 'r') as obj_file:
                obj_dict = json.load(obj_file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    cls = eval(class_name)
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
