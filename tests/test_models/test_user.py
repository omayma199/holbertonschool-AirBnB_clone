"""Unit test for the class user"""

import unittest
from  models import user
from models.user  import User
from models.base_model import BaseModel
from uuid import UUID
from models import storage
import datetime

class TestUserClass(unittest.TestCase):
    """TestCityClass test for the city class
    Args:
     unitest(): Propertys for unit testing
    """

    def set(self):
        """Return  to class attribute"""
        User.email= ""
        User.password= ""
        User.first_name= ""
        User.last_name= ""

    def Test_User(self):
        obj = User()
        obj.name ="holbertonschool"
        obj.my_number = 123
        obj.save()
        self.assertEqual(obj.name, "holbertonschool")
        self.assertEqual((obj.my_number, 123))
        self.assertEqual(isinstance(obj.__class__.__name__, "User"))
        self.assertEqual(isinstance(obj.created_at, datetime), True)
        self.assertEqual(isinstance(obj.updated_at, datetime), True)
        self.assertEqual(type(obj.to_dict()), dict)
    
    def test_isinstance(self):
        "Test if user is instance of BaseModel"
        testUser = User()
        self.assertTrue(isinstance(testUser, BaseModel))
    
    def test_attribyte_Type(self):
        """"""
        testUser = User()
        self.assertTrue(type(testUser.email == str))
        self.assertTrue(type(testUser.password ==str))
        self.assertTrue(type(testUser.first_name ==str))
        self.assertTrue(type(testUser.last_name ==str))
if __name__ == '__main__':
    unittest.main()