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
async def create_user(user: User) -> str | None:
    '''create user and return result.
    use status code 409 for resource conflict (duplicate key error)'''

#----------------------- READ --------------------------

@app.get('/users/')
async def read_users(id:str = None) -> UserCollection | User | None:
    '''
    if param id, return user by id
    else return all users
    :raises HTTPException 404 if user not found
    '''

@app.get("/users/{userName}")
async def read_users(userName:str) -> User | None:
    '''read user and return result.
    use status code 404 if user is not found'''

#------------------------ update and delete ------------------

@app.put('/users/{userName}')
async def update_user(userName:str,user:UserUpdate) -> int:
    ''' update user by username and return result'''


@app.put('/users/')
async def update_user(id:str,user:UserUpdate) -> int:
    ''' update user by id and return result'''

    return user_manager.update(id,user)

#---------------- DELETE ----------------

@app.delete('/users/{username}')
async def delete_users(username: str) -> int:
    '''delete users
    :param username: delete by username
        if username == "all" delete all
    :param query: delete by query
    '''


@app.delete('/users/')
async def delete_users(id:str) -> int:
    '''delete users
    :param uid: delete by id
    '''

#--------------- AUTH ----------------

@app.post('/users/authenticate')
async def authenticate_user(ua:UserAuth) -> User:
    '''authenticate user
    if userAuth is valid, return User'''

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)