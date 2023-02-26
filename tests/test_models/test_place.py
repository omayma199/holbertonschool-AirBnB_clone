#!/usr/bin/python3
"""Unit test for the class place"""

import unittest
from  models import place
from models.place import Place
from models.base_model import BaseModel
from uuid import UUID
from models import storage
from datetime import datetime

class TestReviewClass(unittest.TestCase):
    """TestCityClass test for the place class
    Args:
     unitest(): Propertys for unit testing
    """

    def set(self):
        """Return  to class attribute"""
        Place.city_id= ""
        Place.user_id= ""
        Place.name= ""
        Place.description= ""
        Place.number_rooms= 0
        Place.number_bathrooms= 0
        Place.max_guest= 0
        Place.price_by_night= 0
        Place.latitude= 0.0
        Place.longitude= 0.0
        Place.amenity_ids= ""
    def Test_Place(self):
        obj = Place()
        obj.name ="holbertonschool"
        obj.my_number = 123
        obj.save()
        self.assertEqual(obj.name, "holbertonschool")
        self.assertEqual((obj.my_number, 123))
        self.assertEqual(isinstance(obj.__class__.__name__, "Place"))
        self.assertEqual(isinstance(obj.created_at, datetime), True)
        self.assertEqual(isinstance(obj.updated_at, datetime), True)
        self.assertEqual(type(obj.to_dict()), dict)
    
    def test_isinstance(self):
        "Test if user is instance of BaseModel"
        testPlace = Place()
        self.assertTrue(isinstance(testPlace, BaseModel))
    
    def test_attribyte_Type(self):
        """"""
        testPLace = Place()
        self.assertTrue(type(testPLace.city_id == str))
        self.assertTrue(type(testPLace.user_id ==str))
        self.assertTrue(type(testPLace.name ==str))
        self.assertTrue(type(testPLace.description == str))
        self.assertTrue(type(testPLace.number_rooms == int))
        self.assertTrue(type(testPLace.number_bathrooms ==int))
        self.assertTrue(type(testPLace.max_guest == int))
        self.assertTrue(type(testPLace.price_by_night == int))
        self.assertTrue(type(testPLace.latitude == float)) 
        self.assertTrue(type(testPLace.longitude == float)) 
        self.assertTrue(type(testPLace.amenity_ids ==  list)) 
                   
if __name__ == '__main__':
    unittest.main()