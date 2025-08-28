from bson import ObjectId
import pymongo
from pymongo.errors import DuplicateKeyError

from db_manager import DBManager

class UserManager(DBManager):

    def __init__(self, conn_str:str):
        '''connect to db server and set self.col'''
        
        super().__init__(conn_str,'user_database','users')
        self.col.create_index("username", unique=True)
