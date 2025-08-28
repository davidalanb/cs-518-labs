import unittest

from pymongo.errors import DuplicateKeyError

# from db_manager import DBManager

from user_manager import UserManager
from user_models import *

conn_str = "YOUR URL HERE"
um = UserManager(conn_str)

class TestUserManager(unittest.TestCase):

    # @unittest.skip
    def test_basic(self):
        ''' Initialize, create user, read_by_id user'''

        um.delete_all()

        u = User(username='joe',password='pw')
        uid = um.create(u.model_dump())

        u = um.read_by_id(uid)
        self.assertIsNotNone(u)

    # @unittest.skip
    def test_unique(self):
        ''' try to create a user with the same username twice'''

        um.delete_all()

        u = User(username='joe',password='pw')
        uid = um.create(u.model_dump())

        try:
            uid = um.create(u.model_dump())
        except DuplicateKeyError as e:
            # print(e)
            pass
        else:
            raise Exception('should have been an error here')

    # @unittest.skip
    def test_reads(self):
        ''' read all, read by username'''

        um.delete_all()

        u = User(username='joe',password='pw')
        uid = um.create(u.model_dump())

        u = User(username='jane',password='pw')
        uid = um.create(u.model_dump())

        us = um.read_all()
        self.assertEqual(len(us),2)

        q = UserQuery(username='jane')
        us = um.read(q.model_dump())

        u_out = User(**us[0])
        self.assertEqual(u_out.username,'jane')

    # @unittest.skip
    def test_update(self):
        ''' update password '''

        um.delete_all()

        u = User(username='joe',password='pw')
        uid = um.create(u.model_dump())

        updates = UserUpdate(password='newpw')
        um.update(uid,updates.model_dump())

        u = um.read_by_id(uid)
        u = User(**u)
        self.assertEqual(u.password,'newpw')

    # @unittest.skip
    def test_delete(self):
        '''reset, create, delete, read'''

        um.delete_all()

        u = User(username='joe',password='pw')
        uid = um.create(u.model_dump())

        result = um.delete_by_id(uid)
        self.assertEqual(result,1)

        u = um.read_by_id(uid)
        self.assertIsNone(u)

if __name__ == '__main__':
    unittest.main()
