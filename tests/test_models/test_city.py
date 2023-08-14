#!/usr/bin/python3
"""This is the city test cases"""

from models.base_model import BaseModel
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """This is the unittest case for the city class"""

    def test_instance(self):
        ct = City()
        self.assertIsInstance(ct, City)

    def test_subclass(self):
        self.assertTrue(issubclass(City, BaseModel))


if __name__ == "__main__":
    unittest.main()
