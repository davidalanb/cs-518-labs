from UserManager import UserManager
from user_models import *
#from pydantic_core._pydantic_core import ValidationError
import unittest

conn_str = "mongodb://localhost:27017/"
um = UserManager(conn_str)

class TestUserManager(unittest.TestCase):

    def test_basic(self):
        ''' reset, create user, read user by id'''
        1/0

    @unittest.skip
    def test_notfound(self):
        ''' try to read user with invalid id, assert no user'''
        self.assertEqual(True,False)

    def test_unique(self):
        ''' reset, create twice with same username '''
        self.assertTrue(False)

    def test_read_all(self):
        ''' reset, create many, read all, verify'''

    def test_set_address(self):
        ''' reset, create user, set address, read and verify address set'''
        
    def test_delete(self):
        ''' reset, create user, read user, assert no user'''

if __name__=="__main__":
    unittest.main()
