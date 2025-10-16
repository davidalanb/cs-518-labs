import json
import requests
import responses # Import the library
import unittest

from clients.user_client import UserClient
from clients.exceptions import *

# Your client code remains the same

class TestAPIClientWithResponses(unittest.TestCase):

    @classmethod
    def setUpClass(cls):        
        cls.client = UserClient("https://api.example.com")
        cls.DUMMY_USER = {'username':'dummy','password':'pw'}
        cls.DUMMY_COLLECTION = {"users": [cls.DUMMY_USER]}

    #---------------------------- create ------------------------------

    @responses.activate # Decorator to activate responses for the test
    def test_create(self):

        # 1. Register the mock response
        responses.add(
            method=responses.POST,
            url='https://api.example.com/users',
            json="userid1234",
            status=200
        )

        uid = self.client.create(self.DUMMY_USER)
        self.assertEqual(uid,'userid1234')

        # verify the API calls made 
        self.assertEqual(len(responses.calls), 1, "There should be exactly one HTTP request made.")
        request = responses.calls[0].request 
        self.assertEqual(request.method, 'POST')
        self.assertEqual(request.url, 'https://api.example.com/users')
        
        # verify the request body
        sent_body = json.loads(request.body.decode('utf-8'))
        self.assertEqual(sent_body, self.DUMMY_USER, "The request body should match self.DUMMY_USER.")        

    @responses.activate
    def test_conflict(self):

        # 1. Register the mock response
        responses.add(
            method=responses.POST,
            url='https://api.example.com/users',
            body="username taken",
            status=409
        )

        with self.assertRaises(ResourceConflict):

            # assume DUMMY_USER has already been added
            uid = self.client.create(self.DUMMY_USER)

    #---------------------------- read ------------------------------

    @responses.activate 
    def test_read_all(self):

        # 1. Register the mock response
        responses.add(
            method=responses.GET,
            url='https://api.example.com/users/',
            json=self.DUMMY_COLLECTION,
            status=200
        )
        
        # 2. Call the function under test (it will be intercepted)
        data = self.client.read_all()
        self.assertEqual(data[0], self.DUMMY_USER)
        
        # You can also check if the call was made
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.url, 'https://api.example.com/users/')

    @responses.activate
    def test_read_by_id(self):

        responses.add(
            method=responses.GET,
            url='https://api.example.com/users/?id=uid1234',
            json=self.DUMMY_USER,
            status=200
        )
        
        u = self.client.read_by_id('uid1234')        
        self.assertEqual(u,self.DUMMY_USER)

    @responses.activate 
    # @unittest.skip
    def test_read_by_username(self):
        
        responses.add(
            method=responses.GET,
            url='https://api.example.com/users/dummy',
            json=self.DUMMY_USER, 
            status=200
        )
        
        u = self.client.read_by_username('dummy')
        self.assertEqual(u,self.DUMMY_USER)

    @responses.activate 
    def test_user_not_found(self):
        
        responses.add(
            method=responses.GET,
            url='https://api.example.com/users/user999',
            body='{"error": "Not Found"}', # Use 'body' for text response
            status=404
        )
        
        with self.assertRaises(ResourceNotFound):
            self.client.read_by_username('user999')

    #---------------------- update / delete

    @responses.activate
    def test_update(self):

        # --- Mock the Response ---
        responses.add(
            method=responses.PUT,
            url='https://api.example.com/users/?id=uid1234',
            json=1,
            status=200
        )
        
        # run the code and verify the response
        n = self.client.update('uid1234', self.DUMMY_USER)
        self.assertEqual(n, 1, "The client method should return the expected count.")
        
        # verify the API calls made 
        self.assertEqual(len(responses.calls), 1, "There should be exactly one HTTP request made.")
        request = responses.calls[0].request 
        self.assertEqual(request.method, 'PUT')
        self.assertEqual(request.url, 'https://api.example.com/users/?id=uid1234')
        
        # verify the request body
        sent_body = json.loads(request.body.decode('utf-8'))
        self.assertEqual(sent_body, self.DUMMY_USER, "The request body should match self.DUMMY_USER.")

    @responses.activate
    def test_delete(self):

        # --- Mock the Response ---
        responses.add(
            method=responses.DELETE,
            url='https://api.example.com/users/?id=uid1234',
            json=1,
            status=200
        )
        
        # run the code and verify the response
        n = self.client.delete_by_id('uid1234')
        self.assertEqual(n, 1, "The client method should return the expected count.")
        
        # verify the API calls made 
        self.assertEqual(len(responses.calls), 1, "There should be exactly one HTTP request made.")
        request = responses.calls[0].request 
        self.assertEqual(request.method, 'DELETE')
        self.assertEqual(request.url, 'https://api.example.com/users/?id=uid1234')

    @responses.activate
    def test_authenticate(self):

        # --- Mock the Response ---
        responses.add(
            method=responses.POST,
            url='https://api.example.com/users/authenticate',
            json=self.DUMMY_USER,
            status=200
        )
        
        # run the code and verify the response
        u = self.client.authenticate(self.DUMMY_USER)
        self.assertEqual(u, self.DUMMY_USER)
        
        # verify the API calls made 
        self.assertEqual(len(responses.calls), 1, "There should be exactly one HTTP request made.")
        request = responses.calls[0].request 
        # self.assertEqual(request.method, 'POST')
        # self.assertEqual(request.url, 'https://api.example.com/users/authenticate')

        # verify the request body
        sent_body = json.loads(request.body.decode('utf-8'))
        self.assertEqual(sent_body, self.DUMMY_USER, "The request body should match self.DUMMY_USER.")


if __name__ == '__main__':
    unittest.main()