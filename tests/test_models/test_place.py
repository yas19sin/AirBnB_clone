#!/usr/bin/python3
""" unit test for Review """
import unittest
from models.place import Place
from datetime import datetime


class PlaceTestCase(unittest.TestCase):
    """ class for place test """

    def test_place(self):
        """existince"""
        iNew = Place()
        self.assertTrue(hasattr(iNew, "id"))
        self.assertTrue(hasattr(iNew, "created_at"))
        self.assertTrue(hasattr(iNew, "updated_at"))
        self.assertTrue(hasattr(iNew, "city_id"))
        self.assertTrue(hasattr(iNew, "user_id"))
        self.assertTrue(hasattr(iNew, "name"))
        self.assertTrue(hasattr(iNew, "description"))
        self.assertTrue(hasattr(iNew, "number_rooms"))
        self.assertTrue(hasattr(iNew, "number_bathrooms"))
        self.assertTrue(hasattr(iNew, "max_guest"))
        self.assertTrue(hasattr(iNew, "price_by_night"))
        self.assertTrue(hasattr(iNew, "latitude"))
        self.assertTrue(hasattr(iNew, "longitude"))
        self.assertTrue(hasattr(iNew, "amenity_ids"))

        """type test"""
        self.assertIsInstance(iNew.id, str)
        self.assertIsInstance(iNew.created_at, datetime)
        self.assertIsInstance(iNew.updated_at, datetime)
        self.assertIsInstance(iNew.city_id, str)
        self.assertIsInstance(iNew.user_id, str)
        self.assertIsInstance(iNew.name, str)
        self.assertIsInstance(iNew.description, str)
        self.assertIsInstance(iNew.number_rooms, int)
        self.assertIsInstance(iNew.number_bathrooms, int)
        self.assertIsInstance(iNew.max_guest, int)
        self.assertIsInstance(iNew.price_by_night, int)
        self.assertIsInstance(iNew.latitude, float)
        self.assertIsInstance(iNew.longitude, float)
        self.assertIsInstance(iNew.amenity_ids, list)


if __name__ == '__main__':
    unittest.main()
