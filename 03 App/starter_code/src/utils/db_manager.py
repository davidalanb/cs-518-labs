# from bson import ObjectId
import pymongo
# from pydantic import BaseModel

class DBManager:

    #------------- init and reset --------------

    def __init__(self, conn_str:str, db, col):
        '''connect to db server and set self.col'''
        
        self.myclient = pymongo.MongoClient(conn_str)
        mydb = self.myclient[db]
        self.col = mydb[col]

    def close(self):
        self.myclient.close()

    def create_index(self,index,unique=True):
        self.col.create_index(index, unique=unique) 

    def delete_all(self) -> int:
        ''' delete all
        :returns: deleted_count
        '''

        result = self.col.delete_many({})
        return result.deleted_count  
    
    #------------------ CRUD -----------------

    ''' USE YOUR CODE FROM LAST WEEK'''

    # def create(self, d: dict) -> str:
    #     '''create user
    #     :param d: data to insert into db
    #     :returns: id
    #     '''

    # def read_by_id(self, obj_id:str) -> dict:
    #     '''read user by id 
    #     :param obj_id: 
    #     :returns: data retrieved, or None
    #     '''
        
    # def read(self,query:dict) -> list:
    #     '''read many by query
    #     :params: query
    #     :returns: data retrieved
    #     '''
    
    # def read_all(self) -> list:
    #     '''read all
    #     :returns: data
    #     '''

    # def update(self,obj_id: str,updates:dict) -> int:
    #     ''' update by id 
    #     :param obj_id: 
    #     :param updates: 
    #     :returns: modified_count
    #     '''

    # def delete_by_id(self,obj_id: str):
    #     ''' delete by id
    #     :params: obj_id
    #     :returns: deleted_count (int)
    #     '''
    
    # def delete(self,query:dict) -> str:
    #     ''' delete many by query         
    #     :params: query 
    #     :returns: deleted_count 
    #     '''