#!/usr/bin/python3
""" unit test for State """
import unittest
from models.state import State
from datetime import datetime


class StateTestCase(unittest.TestCase):
    """ class for State test """

    def test_state(self):
        """existince"""
        iNew = State()
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
