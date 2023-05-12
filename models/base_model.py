#!/usr/bin/python3

import uuid

from datetime import datetime


class BaseModel:
    """
    Base class that defines common attributes and methods for
    other classes.
    """

    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.

        The instance is asssigned a unique id using `uuid.uuid(4)`
        and the `created_at` and `updated_at` attributes are set to
        the current datetime.
        """
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
