import json
import bcrypt
import unittest
from datetime import datetime 
from icecream import ic
from nbformat import ValidationError
# from fastapi.testclient import TestClient

from app_src.clients.user_client import UserClient
from app_src.clients.exceptions import *

# from main import app

from app_src.config import INTEGRATION_TEST_CONFIG

api_url = INTEGRATION_TEST_CONFIG.API_URL
# api_url = "http://localhost:8000"

class TestUserClient(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        '''run once'''

        self.client = UserClient(api_url)

        self.client.delete_all()

    def setUp(self):
        print(self.id())

    def tearDown(self):
        self.client.delete_all()
        pass

    #-------------------- BASE ----------------

    # @unittest.skip
    def test_create_read_all(self):
        '''create user, read all 
        assert that user is there'''

        ms = datetime.now().microsecond
        un = f"user{ms}"

        uid = self.client.create({
            'username':un,
            'password':"pw"
        })
        # print(res.text)

        user_list = self.client.read_all()
        # res_data = json.loads(res.text)

        self.assertEqual(user_list[-1].get('username'),un)

    #-------------------- CREATE ----------------

    # @unittest.skip
    def test_bad_create(self):
        '''validating requests'''

        with self.assertRaises(ValidationError):
            res = self.client.create({
                'username':"user"
            })       
        

    # @unittest.skip
    def test_duplicate(self):
        '''duplicate username should return 409'''

        with self.assertRaises(ResourceConflict):
            res = self.client.create({
                'username':"admin",
                'password':"pw"
            })
    # #-------------------- READ ----------------

    # @unittest.skip
    def test_read_by_username(self):

        u = self.client.read_by_username('admin')

        self.assertEqual(u.get('username'),'admin')

    def test_username_not_found(self):
        '''user not found should return 404'''

        with self.assertRaises(ResourceNotFound):
            res = self.client.read_by_username('nosuchuser')

    # @unittest.skip
    def test_read_by_id(self):

        id = self.client.create({
            'username':'test',
            'password':'test'
        })
        u = self.client.read_by_id(id)
        print(u)
        self.assertEqual(u.get('username'),'test')

    #-------------------- UPDATE ----------------

    # @unittest.skip
    def test_update_password(self):

        ms = datetime.now().microsecond
        un = f"user{ms}"

        uid = self.client.create({
            'username':un,
            'password':"pw"
        })

        # u = self.client.read_by_username(un)
        # uid = u.get('id')

        n = self.client.update(uid, {'password':"new"})
        self.assertEqual(n,1)

        u = self.client.read_by_username(un)
        # print(u)

        # # you can just do assertEqual here
        # self.assertEqual(u.get('password'),'new')

        # Do this only if you're hashing your pw (bonus for auth lab)
        self.assertTrue(verify_password('new',u.get('password')))

    #-------------------- DELETE ----------------

    def test_delete_user(self):
        '''test delete user by username'''

        ms = datetime.now().microsecond
        un = f"user{ms}"

        res = self.client.create({
            'username':un,
            'password':"pw"
        })

        n = self.client.delete({'username':un})
        self.assertEqual(n,1)

        with self.assertRaises(ResourceNotFound):
            u = self.client.read_by_username(un)

    #-------------------- AUTH ----------------

    # @unittest.skip
    def test_authenticate(self):

        u = self.client.authenticate({
            'username':'admin',
            'password':'admin'
        })
        self.assertEqual(u.get('username'),'admin')

# def hash_password(pw):
#     return bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt()) 

def verify_password(plain_password: str, hashed_password: str):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

if __name__ == '__main__':
    unittest.main()


