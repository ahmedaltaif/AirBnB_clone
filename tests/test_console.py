#!/usr/bin/python3

"""Defines a class Test HBNB command for HBNB command class/ console"""
import unittest
import pep8
import console
from console import HBNBCommand


class Test_HBNB_Command(unittest.TestCase):
    """Tests for HBNB command documentation"""

    def test_console_pep8(self):
        """Test if console.py conforms to PEP8 guidelines."""

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["console.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_conforms_pep8(self):
        """Test case that tests/test_console.py conforms to PEP8 guidelines."""

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_console.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_module_str(self):
        """Tests case for the module"""

        self.assertTrue(len(console.__doc__) >= 1)

    def test_class_str(self):
        """Tests case for HBNB command class."""

        self.assertTrue(len(HBNBCommand.__doc__) >= 1)
