#!/usr/bin/python3
"""This is the test for the user class"""

from models.user import User
from models.base_model import BaseModel
import unittest


class TestUser(unittest.TestCase):
    """This is the unittest for the User class"""

    def test_instance(self):
        us = User()

        self.assertIsInstance(us, User)
        self.assertEqual(type(us).__name__, "User")

    def test_subclass(self):
        self.assertTrue(issubclass(User, BaseModel))


if __name__ == "__main__":
    unittest.main()
