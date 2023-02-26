#!/usr/bin/python3
"""Unit test for the class review"""

import unittest
from  models import review
from models.review  import Review
from models.base_model import BaseModel
from uuid import UUID
from models import storage
from datetime import datetime

class TestReviewClass(unittest.TestCase):
    """TestCityClass test for the city class
    Args:
     unitest(): Propertys for unit testing
    """

    def set(self):
        """Return  to class attribute"""
        Review.place_id= ""
        Review.user_id= ""
        Review.text= ""
    def Test_Review(self):
        obj = Review()
        obj.name ="holbertonschool"
        obj.my_number = 123
        obj.save()
        self.assertEqual(obj.name, "holbertonschool")
        self.assertEqual((obj.my_number, 123))
        self.assertEqual(isinstance(obj.__class__.__name__, "Review"))
        self.assertEqual(isinstance(obj.created_at, datetime), True)
        self.assertEqual(isinstance(obj.updated_at, datetime), True)
        self.assertEqual(type(obj.to_dict()), dict)
    
    def test_isinstance(self):
        "Test if user is instance of BaseModel"
        testReview = Review()
        self.assertTrue(isinstance(testReview, BaseModel))
    
    def test_attribyte_Type(self):
        """"""
        testReview = Review()
        self.assertTrue(type(testReview.place_id == str))
        self.assertTrue(type(testReview.user_id ==str))
        self.assertTrue(type(testReview.text ==str))
        
if __name__ == '__main__':
    unittest.main()