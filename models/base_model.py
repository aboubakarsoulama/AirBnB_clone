#!/usr/bin/python3
"""A module that implements the BaseModel class"""
import cmd
from uuid import uuid4
from datetime import datetime


class BaseModel(cmd.Cmd):
    """A class that defines all common attributes/methods for other classes"""

    def __init__(self):
        """Initialize the BaseModel class"""

        super().__init__()
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns the string representation of BaseModel object."""
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Updates 'self.updated_at' with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance:

        - only instance attributes set will be returned
        - a key __class__ is added with the class name of the object
        - created_at and updated_at must be converted to string object in ISO
        object
        """

        attr_set = {k: v for k, v in vars(self).items()
                    if not k.startswith("_")}
        attr_set["__class__"] = type(self).__name__
        attr_set["created_at"] = attr_set["created_at"].isoformat()
        attr_set["updated_at"] = attr_set["updated_at"].isoformat()
        return attr_set
