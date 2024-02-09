#!/usr/bin/python3
    """
    The FileStorage class
    """

import os
from models.base_model import BaseModel
import json

class FileStorage:
    """
    FileStorage class that serializes instances to a JSON file and deserializes
    JSON file to instances:
    """

     def all(self):
        """
        Function that return the dictionary object
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Function that add elements in the dictionary.
        Args:
            obj: The object to set with key <obj class name>.id
        """
        if ins:
            FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = ins

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        new_dictionary = {}
        for keys, values in FileStorage.__objects.items():
            new_dictionary[keys] = values.to_dict()

        with open(FileStorage.__file_path, 'w') as obj:
            json.dump(new_dictionary)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                new_object_dict = json.load(file)
            for key, val in new_object_dict.items():
                cls_name = val['__class__']
                module = sys.modules[__name__]
                cls = getattr(module, cls_name)
                obj = cls(**val)  
                self.__objects[key] = obj
