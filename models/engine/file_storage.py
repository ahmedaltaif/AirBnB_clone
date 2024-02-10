#!/usr/bin/python3

"""The FileStorage class"""

import os
import json
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


class FileStorage:
    """
    FileStorage class that serializes instances to a JSON file and deserializes
    JSON file to instances
    """
    def all(self):
        """a function that return the dictionary object"""

        return FileStorage.__objects

    def new(self, obj):
        """a function that add elements in the dictionary.
        Args:
            obj: The object to set with key <obj class name>.id
        """
        if ins:
            FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = ins

    def save(self):
        """function to serializes __objects to JSON file (path: __file_path)
        """
        new_dictionary = {}
        for keys, values in FileStorage.__objects.items():
            new_dictionary[keys] = values.to_dict()

        with open(FileStorage.__file_path, 'w') as obj:
            json.dump(new_dictionary)

    def reload(self):
        """Deserializes the JSON file to __objects"""

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as file:
                new_object_dict = json.load(file)
            for keys, val in new_object_dict.items():
                FileStorage.__objects[keys] = eval(val['__class__'])(**val)
