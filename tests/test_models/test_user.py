#!/usr/bin/python3
""" unit test for User """
import unittest
from models.user import User
from datetime import datetime


class UserTestCase(unittest.TestCase):
    """ class for User test """

    def test_user(self):
        """existince"""
        iNew = User()
        self.assertTrue(hasattr(iNew, "id"))
        self.assertTrue(hasattr(iNew, "created_at"))
        self.assertTrue(hasattr(iNew, "updated_at"))
        self.assertTrue(hasattr(iNew, "email"))
        self.assertTrue(hasattr(iNew, "password"))
        self.assertTrue(hasattr(iNew, "first_name"))
        self.assertTrue(hasattr(iNew, "last_name"))

        """type test"""
        self.assertIsInstance(iNew.id, str)
        self.assertIsInstance(iNew.created_at, datetime)
        self.assertIsInstance(iNew.updated_at, datetime)
        self.assertIsInstance(iNew.email, str)
        self.assertIsInstance(iNew.password, str)
        self.assertIsInstance(iNew.first_name, str)
        self.assertIsInstance(iNew.last_name, str)


if __name__ == '__main__':
    unittest.main()
