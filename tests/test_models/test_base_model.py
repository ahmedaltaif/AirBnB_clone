#!/usr/bin/python3

""" all tests of the class BaseModel in the base_model module. """
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../')
from models.base_model import BaseModel
from datetime import datetime
from uuid import uuid4
import unittest

class Test_BaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def test_id_isNone(self):
        """Test case for id is not None"""
        model = BaseModel()
        self.assertIsNot(model.id, None)

    def test_class_name(self):
        """test case of the class name"""
        model = BaseModel()
        self.assertEqual(model.__class__.__name__, "BaseModel")

    def test_id_is_string(self):
        """test if the id i string"""
        model = BaseModel()
        self.assertIsInstance(model.id, str)

    def test_id_is_unique(self):
        """test if the id is unique"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_id_length(self):
        """test the lenght of the id"""
        model = BaseModel()
        self.assertEqual(len(model.id), 36)

    def test_create_type(self):
        """test case if what is the type reated_at"""
        model = BaseModel()
        self.assertEqual(type(model.created_at), datetime)

    def test_unique_created_at(self):
        """test created_at modif"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.created_at, model2.created_at)

    def test_dif_updated_at(self):
        """test if updated_at change each time executed"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.updated_at, model2.updated_at)

    def test_created_format(self):
        """Test if time and date created at regular expression"""
        model = BaseModel()
        self.assertRegex(str(model.created_at), '^\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}.\\d{6}')

    def test_update_format(self):
        """Test if updated_at at regular experssion"""
        model = BaseModel()
        self.assertRegex(str(model.updated_at), '^\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}.\\d{6}')

    def test_key_word_args(self):
        """test case of the key word args"""
        model = BaseModel()
        dict_a = model.to_dict()
        model2 = BaseModel(**dict_a)
        self.assertEqual(model.id, model2.id)

    def test_key_word_args_datetime(self):
        """test case key word args datetime"""
        model1 = BaseModel()
        dict_a = model1.to_dict()
        model2 = BaseModel(**dict_a)
        self.assertRegex(str(model2.updated_at), '^\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}.\\d{6}')

    def test_key_word_args_class(self):
        """test kwargs class"""
        model1 = BaseModel()
        dict_a = model1.to_dict()
        model2 = BaseModel(**dict_a)
        self.assertTrue(hasattr(model2, '__class__'))

    def test_class_name_and_id(self):
        """test case string representation"""
        model = BaseModel()
        model.id = 123
        self.assertTrue("[BaseModel] (123)", model.__str__)

    def test_str_updated_at(self):
        """test case of the string representation update_at"""
        model = BaseModel()
        self.assertTrue('updated_at' in str(model), True)

    def test_str_created_at(self):
        """test case for string representation created_at"""
        model = BaseModel()
        self.assertTrue('created_at' in str(model), True)
    
    def test_save_new(self):
        """test case for save method with new string"""
        model = BaseModel()
        model.name = "Hana"
        model.save()
        self.assertEqual(model.name, "Hana")

    def test_save_number(self):
        """test case for save method with new intger"""
        model = BaseModel()
        model.num = 1234
        model.save()
        self.assertEqual(model.num, 1234)

    def test_save_update(self):
        """test case for save update"""
        model = BaseModel()
        model.num = 1
        date1 = model.updated_at
        model.save()
        model.num = 2
        date2 = model.updated_at
        model.save()
        self.assertNotEqual(date1, date2)

    def test_save_updatefile(self):
        """test case for the information are really saved in the file"""
        model = BaseModel()
        model.save()
        with open("file.json", "r", encoding="utf-8") as myfile:
            self.assertIn("BaseModel." + model.id, myfile.read())

    def test_dict_return(self):
        """test case for the to_dict method"""
        model = BaseModel()
        my_dict = model.to_dict()
        self.assertEqual(type(my_dict), dict)

    def test_create_dict(self):
        """test if the dictionary was saved by to_dict"""
        model = BaseModel()
        self.assertEqual(type(model.__dict__), dict)

    def test_dict_type(self):
        """test case for dictionary egal __dict__"""
        model = BaseModel()
        self.assertEqual(type(model.__dict__), type(model.to_dict()))

    def test_keys(self):
        """ test case for keys"""
        model = BaseModel()
        self.assertIn("id", model.to_dict())
        self.assertIn("created_at", model.to_dict())
        self.assertIn("updated_at", model.to_dict())
        self.assertIn("__class__", model.to_dict())

if __name__ == '__main__':
    unittest.main()
