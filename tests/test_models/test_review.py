#!/usr/bin/python3
"""This is the test case for the review class"""

from models.base_model import BaseModel
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """Thsi is the class for the unittest of the Review class"""

    def test_instance(self):
        rv = Review()
        self.assertIsInstance(rv, Review)

    def test_subclass(self):
        self.assertTrue(issubclass(Review, BaseModel))


if __name__ == "__main__":
    unittest.main()
