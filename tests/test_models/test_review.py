#!/usr/bin/python3
""" unit test for Review """
import unittest
from models.review import Review
from datetime import datetime


class ReviewTestCase(unittest.TestCase):
    """ class for Review test """

    def test_review(self):
        """existince"""
        iNew = Review()
        self.assertTrue(hasattr(iNew, "id"))
        self.assertTrue(hasattr(iNew, "created_at"))
        self.assertTrue(hasattr(iNew, "updated_at"))
        self.assertTrue(hasattr(iNew, "place_id"))
        self.assertTrue(hasattr(iNew, "user_id"))
        self.assertTrue(hasattr(iNew, "text"))

        """type test"""
        self.assertIsInstance(iNew.id, str)
        self.assertIsInstance(iNew.created_at, datetime)
        self.assertIsInstance(iNew.updated_at, datetime)
        self.assertIsInstance(iNew.place_id, str)
        self.assertIsInstance(iNew.user_id, str)
        self.assertIsInstance(iNew.text, str)


if __name__ == '__main__':
    unittest.main()
