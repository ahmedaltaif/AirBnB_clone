#!/usr/bin/python3

"""Definition of a class Base"""


from uuid import uuid4
from datetime import datetime
import models


class BaseModel:

    """a class that defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """
        Function that initialize the instance of BaseModel
        """
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for keys, values in kwargs.items():
                if keys in ['created_at', 'updated_at']:
                    values = datetime.strptime(values, "%Y-%m-%dT%H:%M:%S.%f")
                if keys != '__class__':
                    setattr(self, keys, values)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Function that return the string representation.
        should print: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute updated_at with
        the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        obj_dictionary = {"__class__": self.__class__.__name__}
        for keys, values in self.__dict__.items():
            if keys in ['created_at', 'updated_at']:
                obj_dictionary[keys] = values.isoformat()
            else:
                obj_dictionary[keys] = values
        return obj_dictionary
