#!/usr/bin/python3
"""Unittest module for Amenity"""
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """testing the Amenity class"""

def test_str(self):
        """Test case the string output of the class"""
        a = Amenity()
        self.assertEqual(str(a), f"[Amenity] ({a.id}) {a.__dict__}")


if __name__ == '__main__':
    unittest.main()
