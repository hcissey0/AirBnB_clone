#!/usr/bin/python3
"""This is the test for the amenity class"""

from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """This is the amenity class unittest case"""

    def test_instance(self):
        am = Amenity()

        self.assertIsInstance(am, Amenity)

    def test_subclass(self):
        self.assertTrue(issubclass(Amenity, BaseModel))


if __name__ == "__main__":
    unittest.main()
