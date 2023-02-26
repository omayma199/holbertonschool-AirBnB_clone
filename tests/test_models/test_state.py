"""Unit test for the class state"""

import unittest
from  models import state
from models.state  import State
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
        State.name=""
        
    def test_State(self):
        obj = State()
        obj.name ="holbertonschool"
        obj.number = 123
        obj.save()
        self.assertEqual(obj.name, "holbertonschool")
        self.assertEqual((obj.number, 123))
        self.assertEqual(isinstance(obj.__class__.__name__, "State"))
        self.assertEqual(isinstance(obj.created_at, datetime), True)
        self.assertEqual(isinstance(obj.updated_at, datetime), True)
        self.assertEqual(type(obj.to_dict()), dict)

    def test_isinstance(self):
        "Test if user is instance of BaseModel"
        testState = State()
        self.assertTrue(isinstance(testState, BaseModel))
    
    def test_attribyte_Type(self):
        """"""
        testState = State()
        self.assertTrue(type(testState.name) == str)
        

if __name__ == '__main__':
    unittest.main()