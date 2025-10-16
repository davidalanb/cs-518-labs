import json
from icecream import ic
import requests as rq

from .exceptions import *

class UserClient:
    ''' connects to the API '''

    #----------- init and reset (delete_all)----------------

    def __init__(self, url:str):
        self.url = url

    def delete_all(self ) -> int:
        
        res = rq.delete(f"{self.url}/users/all")
        return int(res.text)

    #-------------- Create -------------------------

    def create(self, user: dict ) -> str:
        '''takes a dict, makes a POST request to /users
        
        :params user: dict, data to pass to request as json
        :returns: id of created user
        :raises ResourceConflict: if 409 from server
        :raises ValidationError: if 422 from server'''
        
    #----------------Read ----------------

    def read_all(self) -> list:
        '''
        get all users
        :returns: list of users
        '''

    def read_by_id(self, uid: str ) -> dict:
        '''get user by id
        
        :returns: user dict
        :raises ResourceNotFound: on 404 '''
        
    def read_by_username(self,un: str) -> dict:
        ''' get user by username

        :param un: username
        :returns: user dict
        :raises ResourceNotFound: on 404
        '''
    
    #------------- update / delete --------------------

    def update(self,id:str,update:dict) -> int:
        '''
        :param id: id of user to update
        :param update: dictionary with fields and new values
        :returns: updated count
        :raises ResourceNotFound: if 404 user not found
        :raises ValidationError: if 422 bad update'''
    
    def delete(self,query:dict) -> int:
        '''
        :returns: deleted count
        :raises ResourceNotFound: if 404
        '''

    # #-------------- auth -----------------------

    def authenticate(self,creds: dict) -> dict:
        '''authenticate user
        
        :param creds: dict with credentials
        :returns: user dict
        :raises AuthenticationError: if 401 auth fails
        '''