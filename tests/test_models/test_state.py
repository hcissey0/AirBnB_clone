#!/usr/bin/python3
"""This is the test cases for the state class"""

from models.base_model import BaseModel
from models.state import State
import unittest


class TestState(unittest.TestCase):
    """This is the testcase class for the state class"""

    def test_instance(self):
        st = State()

        self.assertIsInstance(st, State)

    def test_subclass(self):
        self.assertTrue(issubclass(State, BaseModel))


if __name__ == "__main__":
    unittest.main()
