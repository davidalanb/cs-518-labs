import requests as rq
import unittest
import json
import os

from user_client import UserClient

# url = 'http://127.0.0.1:8000' # FastAPI
# url = 'http://127.0.0.1:7071' # Azure Functions
url = '<YOUR_DEPLOYED_USER_SERVICE_URL>'
client = UserClient(url+'/users/')

class UserManagerAPITests(unittest.TestCase):

    # @unittest.skip
    def test_basic(self):
        '''delete users, create one, read by id'''

        client.delete_all()

        body = {'username':'joe','password':'schmoe'}
        uid = client.create(body)  

        u = client.read_by_id(uid)
        self.assertEqual(u.get('username'),'joe')   

    def test_read_notfound(self):

        client.delete_all()

        try:
            u = client.read_by_id('invalidUid')
            self.assertTrue(False)    
        except rq.exceptions.HTTPError as e:
            self.assertEqual(e.response.status_code,404)
            # print(e.response.text)        
                    
    # @unittest.skip
    def test_duplicate(self):
        '''delete users, then try to create two with same username
        make sure second user returns 409'''

    # @unittest.skip    
    def test_reads(self):
        ''' delete all, create, read all, read by username'''
                   
    # @unittest.skip
    def test_update(self):
        '''delete all, create, update, read'''

    #@unittest.skip
    def test_delete(self):
        '''reset, create, read by username, delete, read'''

if __name__=="__main__":
    unittest.main()