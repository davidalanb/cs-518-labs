from icecream import ic
from pymongo.errors import DuplicateKeyError

from fastapi import FastAPI, HTTPException
import uvicorn

from data.user_models import *
from data.db_manager import DBManager
from data.user_manager import UserManager
from config import USER_CONFIG

db_manager = DBManager(USER_CONFIG.DB_URL, USER_CONFIG.USER_DB, USER_CONFIG.USER_COL)
user_manager = UserManager(db_manager)

app = FastAPI()

print('INFO: server loaded')

@app.get('/info')
async def get_info()->str:
    return "fastapi server"

#---------------- create -------------------

@app.post('/users')
async def create_user(user: User) -> str:
    '''create user and return result.

    :param user: User to create
    :returns: user id
    :raises HTTPException: 422 if username equals 'all' 
    :raises HTTPException: 409 if username is taken'''

#----------------------- READ --------------------------

@app.get('/users/')
async def read_users(username:str = None) -> UserCollection:
    '''
    if query param(s), return matching users
    else return all users

    :param usename: str
    :returns: UserCollection
    '''

@app.get("/users/{userId}")
async def read_user(userId:str) -> User:
    '''read user by id

    :param userId: str
    :returns: User
    :raises HTTPException: 404 if user is not found'''

#------------------------ update and delete ------------------

@app.put('/users/{userId}')
async def update_user(userId:str,user:UserUpdate) -> int:
    ''' update user by id and return result

    :returns: int modified_count
    :raises HTTPException: 404 user not found'''

#---------------- DELETE ----------------

@app.delete('/users/{userId}')
async def delete_user(userId: str) -> int:
    '''delete user by id
    if no id is provided, delete all users

    :raises HTTPException: 404 user not found
    '''

#--------------- AUTH ----------------

@app.post('/users/authenticate')
async def authenticate_user(ua:UserAuth) -> User:
    '''authenticate user
    if userAuth is valid, return User
    
    :param ui: UserAuth with credentials
    :returns: User 
    :raises: 401 if authentication fails'''

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)