import pymongo
from bson import ObjectId

from user_models import *

class UserManager:

    def __init__(self, conn_str:str):
        '''connect to db server and set self.col;
        create unique index'''

    def reset(self):
        ''' drop collection and recreate index'''

    def create_user(self, user:UserIn) -> CreateUserResult:
        '''create user and return result'''
        
    def read_users(self,query={}) -> UserCollection:
        ''' get all users'''

    def read_user(self, user_id: str) -> UserOut | None:
        ''' get user by id '''
    
    def update_user(self, user_id: str, updates:dict) -> UpdateUserResult:
        ''' perform update and return result'''