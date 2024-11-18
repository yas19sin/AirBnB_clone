#!/usr/bin/python3
""" unit test for City """
import unittest
from models.city import City
from datetime import datetime


class CityTestCase(unittest.TestCase):
    """ class for city test """

    def test_city(self):
        """existince"""
        iNew = City()
        self.assertTrue(hasattr(iNew, "id"))
        self.assertTrue(hasattr(iNew, "created_at"))
        self.assertTrue(hasattr(iNew, "updated_at"))
        self.assertTrue(hasattr(iNew, "state_id"))
        self.assertTrue(hasattr(iNew, "name"))

        """type test"""
        self.assertIsInstance(iNew.id, str)
        self.assertIsInstance(iNew.created_at, datetime)
        self.assertIsInstance(iNew.updated_at, datetime)
        self.assertIsInstance(iNew.state_id, str)
        self.assertIsInstance(iNew.name, str)


if __name__ == '__main__':
    unittest.main()
