#!/usr/bin/python3
""" unit test for bases """

import unittest
from models.base_model import BaseModel
import models
import json
import os


class FileStorageTestCase(unittest.TestCase):
    """ class for base test """

    def test_FileStorage_init(self):
        """ DOC DOC DOC """
        _pFile = models.storage._FileStorage__file_path
        _iObjs = models.storage._FileStorage__objects
        """check class attr"""
        self.assertEqual(_pFile, "file.json")
        self.assertIsInstance(_pFile, str)
        self.assertIsInstance(_iObjs, dict)
        iNew = BaseModel()

        """ check if it have methods """
        self.assertTrue(hasattr(iNew, "__init__"))
        self.assertTrue(hasattr(iNew, "__str__"))
        self.assertTrue(hasattr(iNew, "save"))
        self.assertTrue(hasattr(iNew, "to_dict"))

        """test all"""
        self.assertIsInstance(models.storage.all(), dict)
        self.assertNotEqual(models.storage.all(), {})
        """existence id"""
        self.assertTrue(hasattr(iNew, "id"))
        self.assertIsInstance(iNew.id, str)

        """iNew"""
        _ikeyName = "BaseModel."+iNew.id
        self.assertIsInstance(models.storage.all()[_ikeyName], BaseModel)
        self.assertEqual(models.storage.all()[_ikeyName], iNew)
        """ check if object exist by _ikeyName """
        self.assertIn(_ikeyName, models.storage.all())
        """ check if the object found in storage with corrrect id"""
        self.assertTrue(models.storage.all()[_ikeyName] is iNew)

        """save"""
        models.storage.save()
        with open(_pFile, 'r') as file:
            saved_data = json.load(file)
        """ check if object exist by _ikeyName """
        self.assertIn(_ikeyName, saved_data)
        """ check if the value found in json is correct"""
        self.assertEqual(saved_data[_ikeyName], iNew.to_dict())

        """reload"""
        models.storage.all().clear()
        models.storage.reload()
        with open(_pFile, 'r') as file:
            saved_data = json.load(file)
        self.assertEqual(saved_data[_ikeyName],
                         models.storage.all()[_ikeyName].to_dict())

        """file"""
        if os.path.exists(_pFile):
            os.remove(_pFile)
        self.assertFalse(os.path.exists(_pFile))
        models.storage.reload()


if __name__ == '__main__':
    unittest.main()
