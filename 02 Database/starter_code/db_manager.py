from bson import ObjectId
import pymongo
from pydantic import BaseModel

class DBManager:

    def __init__(self, conn_str:str, db, col):
        '''connect to db server and set self.col'''
        
        myclient = pymongo.MongoClient(conn_str)
        mydb = myclient[db]
        self.col = mydb[col]

    def create(self, d: dict):
        '''create user and return inserted_id'''

    def read_by_id(self, obj_id:str):
        '''read user by id and return one'''
        
    def read(self,query:dict):
        '''read by query and return many'''
    
    def read_all(self):
        '''read all and return many'''

    def update(self,obj_id,updates:dict):
        ''' update by id and return modified_count '''

    def delete_by_id(self,obj_id):
        ''' delete by id and return deleted_count '''
    
    def delete(self,query:dict):
        ''' update by query and return deleted_count '''
    
    def delete_all(self):
        ''' delete all and return deleted_count '''     