#!/usr/bin/python3

import uuid

from datetime import datetime


class BaseModel:
    """
    Base class that defines common attributes and methods for
    other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Tuple of arguments
            **kwargs: Dictionary of key-value arguments.
        """
        if kwargs:
            """
            Sets attributes based on the provided kwargs dicts.
            """
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(
                                self, key, datetime.strptime(
                                    value, "%Y-%m-%dT%H:%M:%S.%f"
                                )
                        )
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def save(self):
        """
        Updates the `updated_at` attribute with the current datetime.
        """
        self.upated_at = datetime.now()

    def to_dict(self):
        """
        Converts the instance attribute to a dictionary.

        Returns:
            A dictionary containing all instance attributes, including
            the class name, creation datetime, and update datetime.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        Return an informal string representation of the BaseModel object.

        Returns:
            A string in the format: "[class name] (id) {attribute dictionary}"
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__
        )
