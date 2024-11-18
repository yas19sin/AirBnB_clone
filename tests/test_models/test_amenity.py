#!/usr/bin/python3
""" unit test for Amenity """
import unittest
from models.amenity import Amenity
from datetime import datetime


class CityTestCase(unittest.TestCase):
    """ class for amenity test """

    def test_amenity(self):
        """existince"""
        iNew = Amenity()
        self.assertTrue(hasattr(iNew, "id"))
        self.assertTrue(hasattr(iNew, "created_at"))
        self.assertTrue(hasattr(iNew, "updated_at"))
        self.assertTrue(hasattr(iNew, "name"))

        """type test"""
        self.assertIsInstance(iNew.id, str)
        self.assertIsInstance(iNew.created_at, datetime)
        self.assertIsInstance(iNew.updated_at, datetime)
        self.assertIsInstance(iNew.name, str)


if __name__ == '__main__':
    unittest.main()
