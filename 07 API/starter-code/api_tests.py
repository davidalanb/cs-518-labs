import requests as rq
import unittest
import json

url = 'http://127.0.0.1:8000'

class UserManagerAPITests(unittest.TestCase):

    def test_basic(self):
        '''delete users, create one, read'''

    def test_duplicate(self):
        '''delete users, then try to create two with same username
        make sure second user returns 409'''

    # etc.  similar to your unit tests
        
if __name__=="__main__":
    unittest.main()