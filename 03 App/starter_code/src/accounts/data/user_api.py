from accounts.data.user_manager import UserManager
from accounts.data.user_models import *

class UserAPI:
    '''The UserAPI will always take plain python from the consumer (e.g. dicts, strings). 
    From dicts, it will create model objects and pass those to the UserManager.
    The UserManager will return model objects.  The UserAPI dump those and return dicts.
    '''

    '''USER YOUR CODE FROM LAST WEEK'''

    # def __init__(self, user_manager):
    #     self.um = user_manager

    # def delete_all(self ) -> int:
    #     return self.um.delete_all()

    # #---------------- CRUD ------------------------

    # def create(self, user: dict ) -> str:
    #     '''converts user dict to User object, 
    #     passes to self.um.create and returns result'''

    #     u = User(**user)
    #     return self.um.create(u)

    # def read_by_id(self, uid: str ) -> dict:
    #     '''read using self.um, gets back User or None,
    #     dumps to dict and returns'''

    # def read_all(self) -> list[dict]:
    #     '''read all, gets back UserCollection,
    #     dumps UserCollection to list of dicts'''
    
    # def read(self, query: dict ) -> list[dict]:
    #     ''' converts query to UserQuery, passes to self.um.read
    #     gets back UserCollection, dumps to list of dicts
    #     '''
    
    # def update(self,id:str,update:dict) -> int:
    #     '''converts update to UserUpdate, calls self.um.update,
    #     returns result'''
    
    # def delete_by_id(self,id:str) -> int:
    #     ''' calls self.um.delete_by_id, returns result'''

