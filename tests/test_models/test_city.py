"""Unit test for the class city"""

import unittest
from  models import city
from models.city  import City
from models.base_model import BaseModel
from uuid import UUID
from models import storage
from datetime import datetime

class TestCityClass(unittest.TestCase):
    """TestCityClass test for the city class
    Args:
     unitest(): Propertys for unit testing
    """

    def set(self):
        """Return  to class attribute"""
        City.name=""
        City.state_id=""
    def test_City(self):
        obj = City()
        obj.name ="holbertonschool"
        obj.number = 123
        obj.save()
        self.assertEqual(obj.name, "holbertonschool")
        self.assertEqual((obj.number, 123))
        self.assertEqual(isinstance(obj.__class__.__name__, "City"))
        self.assertEqual(isinstance(obj.created_at, datetime), True)
        self.assertEqual(isinstance(obj.updated_at, datetime), True)
        self.assertEqual(type(obj.to_dict()), dict)

    def test_isinstance(self):
        "Test if user is instance of BaseModel"
        testCity = City()
        self.assertTrue(isinstance(testCity, BaseModel))
    
    def test_attribyte_Type(self):
        """"""
        testCity = City()
        self.assertTrue(type(testCity.name) == str)
        self.assertTrue(type(testCity.state_id) == str)

if __name__ == '__main__':
    unittest.main()