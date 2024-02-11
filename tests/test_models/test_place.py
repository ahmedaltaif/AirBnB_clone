#!/usr/bin/python3

"""Unittest for place.py """

import unittest
import json
import os
from models.place import Place
from models import storage


class TestPlace(unittest.TestCase):
    """Tests `Place` class.
    For interactions with *args and **kwargs, see test_base_model.

    Attributes:
        __objects_backup: copy of current dict of objects
        json_file: filename for JSON file of objects
        json_file_backup: filename for backup of json file
    """
    __objects_backup = storage._FileStorage__objects
    json_file = storage._FileStorage__file_path
    json_file_backup = storage._FileStorage__file_path + '.bup'

    @classmethod
    def setUpClass(cls):
        """Setup for all tests in module."""

        storage._FileStorage__objects = dict()
        if os.path.exists(cls.json_file):
            copy2(cls.json_file, cls.json_file_backup)
            os.remove(cls.json_file)

    @classmethod
    def tearDownClass(cls):
        """Teardown after all tests in module."""

        storage._FileStorage__objects = cls.__objects_backup
        if os.path.exists(cls.json_file_backup):
            copy2(cls.json_file_backup, cls.json_file)
            os.remove(cls.json_file_backup)

    def tearDown(self):
        """teardown method"""
        try:
            del (p1, p2)
        except NameError:
            pass
        storage._FileStorage__objects = dict()
        if os.path.exists(type(self).json_file):
            os.remove(type(self).json_file)

if __name__ == '__main__':
    unittest.main()
