# from blueprints.accounts.data.user_manager import UserManager
# from blueprints.accounts.data.user_models import *

import json
from icecream import ic
import requests as rq

from .exceptions import *


class UserClient:
    ''' connects to the API '''

    #----------- init and reset (delete_all)----------------

    def __init__(self, url:str):
        self.url = url

    # def close(self):
    #     self.um.close()

    def delete_all(self ) -> int:
        
        res = rq.delete(f"{self.url}/users/all")
        return int(res.text)

    #-------------- CRUD -------------------------

    def create(self, user: dict ) -> str:
        '''takes a dict, validates, and passes User to um
        really this should return a dict
        
        :returns id of created user
        :raises ResourceConflict if 409 from server
        :raises ValidationError if 422 from server'''

        res = rq.post(f"{self.url}/users",json=user)

        if res.status_code==200:
            return json.loads(res.text)
        elif res.status_code==409:
            raise ResourceConflict(res)
        elif res.status_code==422:
            raise ValidationError(res)
        
    #--------------------------------

    # def get_usernames(self,uids):
    #     return self.um.get_usernames(uids)

    def read_all(self) -> list:

        res = rq.get(f"{self.url}/users/")
        res_data = json.loads(res.text)

        # print(res_data)

        return res_data.get('users')

    def read_by_id(self, uid: str ) -> dict:
        '''reads, validates, and returns dict'''

        res = rq.get(f"{self.url}/users/",params={'id':uid})

        if res.status_code==200:
            u = json.loads(res.text)
            return u
        
        
    def read_by_username(self,un) -> dict:

        res = rq.get(f'{self.url}/users/{un}')
        # print(res.status_code, res.text)

        if res.status_code==200:
            u = json.loads(res.text) 
            return u
        elif res.status_code==404:
            raise ResourceNotFound(res)   

    # def read(self, query: dict ) -> list:

    #     res = rq.get(f'{self.url}/users/{un}')
    #     # print(res.status_code, res.text)

    #     # self.assertEqual(res.status_code,200)        
    #     u = json.loads(res.text) 
    #     return u  
    
    def update(self,id:str,update:dict) -> int:

        res = rq.put(f'{self.url}/users/',
                        params={'id':id},
                        json=update)
        return int(res.text)
    
    # def delete_by_id(self,id:str) -> int:

    #     return self.um.delete_by_id(id)
    
    def delete(self,query:dict) -> int:

        un = query.get('username')
        if un:
            res = rq.delete(f"{self.url}/users/{un}")
            return int(res.text)
        else:
            raise ValidationError('username required for delete')
        
    # #-------------- login -----------------------

    def authenticate(self,creds: dict) -> dict:

        res = rq.post(f"{self.url}/users/authenticate",json=creds)

        if res.text:
            return json.loads(res.text)



