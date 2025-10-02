from utils.db_manager import DBManager
from accounts.data.user_models import *

# from pymongo.errors import DuplicateKeyError

class UserManager:
    '''The UserManager takes model objects from the UserAPI.  It dumps them and passes them to DBManager for db operations.
    DBManager returns python objects (e.g. dicts, lists).
    UserManager converts those to model objects and passes back to the UserAPI.
    '''

    '''USER YOUR CODE FROM LAST WEEK'''

    # #------------------ init and reset ----------

    # def __init__(self, dbm: DBManager):
    #     '''connect to db server and set self.col'''

    #     self.dbm = dbm
    #     self.dbm.create_index('username')

    # def delete_all(self):
    #     ''' delete all users except admin (for testing)'''

    #     count = self.dbm.delete({'username': {'$ne': 'admin'}})
    #     return count    
    
    # #----------------- CRUD ----------------------

    # def create_user(self,user:User) -> str:
    #     ''' create user
    #     :returns: id as str'''

    #     ud = user.model_dump()
    #     id = self.dbm.create(ud)
    #     return id

    # def read_all(self) -> UserCollection:
    #     ''' read users '''

    # def read_by_id(self,id: str) -> User:
    #     ''' read by id
    #     :returns: User or None'''

    # def read_by_username(self,username: str) -> User:
    #     '''read by username
    #     :returns: User or None'''

    # def update(self,id,q:UserUpdate) -> int:
    #     '''update user
    #     :returns: modified_count'''
        
    # def delete(self,q: UserQuery) -> int:
    #     '''delete user
    #     :returns: deleted_count'''



