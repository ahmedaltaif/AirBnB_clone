#!/usr/bin/python3

"""Definition of a class Base"""

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:

"""a class that defines all common attributes/methods for other classes"""

class BaseModel:
    """ Class that defines properties of base """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string represation of class details."""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update public instance attribute updated_at with current datetime"""

        self.updated_at = datetime.now()

    def to_dict(self):
         """Returns a dictionary containing all key/values of __dict__ of
        the instance.
        """

        return {
            "__class__": self.__class__.__name__,
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            **self.__dict__
        }
