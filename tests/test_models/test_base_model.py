#!/usr/bin/python3
""" unit test for bases """
import json
import unittest
from models.base_model import BaseModel
from datetime import datetime
import models
from io import StringIO
import sys
from unittest.mock import patch
captured_output = StringIO()
sys.stdout = captured_output


class BaseModelTestCase(unittest.TestCase):
    """ class for base test """

    def setUp(self):
        """ class for base test """
        self.filepath = models.storage._FileStorage__file_path
        with open(self.filepath, 'w') as file:
            file.truncate(0)
        models.storage.all().clear()

    def tearDown(self):
        """ class for base test """
        printed_output = captured_output.getvalue()
        sys.stdout = sys.__stdout__

    def test_basemodel_init(self):
        """ class for base test """
        iNew = BaseModel()

        """ check if it have methods """
        self.assertTrue(hasattr(iNew, "__init__"))
        self.assertTrue(hasattr(iNew, "__str__"))
        self.assertTrue(hasattr(iNew, "save"))
        self.assertTrue(hasattr(iNew, "to_dict"))

        """existince"""
        self.assertTrue(hasattr(iNew, "id"))
        self.assertTrue(hasattr(iNew, "created_at"))
        self.assertTrue(hasattr(iNew, "updated_at"))

        """type test"""
        self.assertIsInstance(iNew.id, str)
        self.assertIsInstance(iNew.created_at, datetime)
        self.assertIsInstance(iNew.updated_at, datetime)

        """ check if save in storage """
        _ikeyName = "BaseModel."+iNew.id
        """ check if object exist by _ikeyName """
        self.assertIn(_ikeyName, models.storage.all())
        """ check if the object found in storage with corrrect id"""
        self.assertTrue(models.storage.all()[_ikeyName] is iNew)

        """ Test update """
        iNew.name = "My First Model"
        iNew.my_number = 89
        self.assertTrue(hasattr(iNew, "name"))
        self.assertTrue(hasattr(iNew, "my_number"))
        self.assertTrue(hasattr(models.storage.all()[_ikeyName], "name"))
        self.assertTrue(hasattr(models.storage.all()[_ikeyName], "my_number"))

        """check if save() update update_at time change"""
        old_time = iNew.updated_at
        iNew.save()
        self.assertNotEqual(old_time, iNew.updated_at)
        self.assertGreater(iNew.updated_at, old_time)

        """ check if init it call: models.storage.save() """
        with patch('models.storage.save') as mock_function:
            obj = BaseModel()
            obj.save()
            mock_function.assert_called_once()

        """check if it save in json file"""
        _ikeyName = "BaseModel."+iNew.id
        with open(self.filepath, 'r') as file:
            saved_data = json.load(file)
        """ check if object exist by _ikeyName """
        self.assertIn(_ikeyName, saved_data)
        """ check if the value found in json is correct"""
        self.assertEqual(saved_data[_ikeyName], iNew.to_dict())

    def test_basemodel_init2(self):
        """ class for base test """

        iNew = BaseModel()
        iNew.name = "John"
        iNew.my_number = 89
        iNew2 = BaseModel(**iNew.to_dict())
        self.assertEqual(iNew.id, iNew2.id)
        self.assertEqual(iNew.name, "John")
        self.assertEqual(iNew.my_number, 89)
        self.assertEqual(iNew.to_dict(), iNew2.to_dict())

    def test_basemodel_init3(self):
        """ DOC DOC DOC """
        iNew = BaseModel()
        iNew2 = BaseModel(iNew.to_dict())
        self.assertNotEqual(iNew, iNew2)
        self.assertNotEqual(iNew.id, iNew2.id)
        self.assertTrue(isinstance(iNew2.created_at, datetime))
        self.assertTrue(isinstance(iNew2.updated_at, datetime))

        iNew = BaseModel()

        self.assertEqual(
            str(iNew),  "[BaseModel] ({}) {}".format(iNew.id, iNew.__dict__))

        old_time = iNew.updated_at
        iNew.save()
        self.assertGreater(iNew.updated_at, old_time)


if __name__ == '__main__':
    unittest.main()
