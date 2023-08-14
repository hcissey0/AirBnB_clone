#!/usr/bin/python3
"""This is the test for the Place class"""

from models.base_model import BaseModel
from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    """Thist is the unittest case for the Place class"""

    def test_instance(self):
        pl = Place()
        self.assertIsInstance(pl, Place)

    def test_subclass(self):
        self.assertTrue(issubclass(Place, BaseModel))


if __name__ == "__main__":
    unittest.main()
