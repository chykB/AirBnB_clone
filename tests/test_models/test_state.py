#!/usr/bin/python3
<<<<<<< HEAD
"""Test suite for the State class of the models.state module"""
import unittest

from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def setUp(self):
        self.state = State()

    def test_state_is_a_subclass_of_basemodel(self):
        self.assertTrue(issubclass(type(self.state), BaseModel))

    def test_attr_is_a_class_attr(self):
        self.assertTrue(hasattr(self.state, "name"))

    def test_class_attrs(self):
        self.assertIs(type(self.state.name), str)
        self.assertFalse(bool(self.state.name))
=======
"""Unittest module for the State Class."""

import unittest
from datetime import datetime
import time
from models.state import State
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    """Test Cases for the State class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests instantiation of State class."""

        b = State()
        self.assertEqual(str(type(b)), "<class 'models.state.State'>")
        self.assertIsInstance(b, State)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of State class."""
        attributes = storage.attributes()["State"]
        o = State()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

if __name__ == "__main__":
    unittest.main()
>>>>>>> 8b93a145d511c2a06b597e8d5ef4a873e261dcc6
