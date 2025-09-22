from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from typing import Union

from user_models import *
#from UserManager import UserManager

conn_str = "mongodb://localhost:27017/"

app = FastAPI()

print('INFO: server loaded')

@app.post('/users', responses={409: {"model": OperationResult}})
async def create_user(user: UserIn) -> CreateUserResult:
    '''create user and return result.
    use status code 409 for resource conflict (duplicate key error)'''

@app.get('/users')
async def read_users() -> UserCollection:
    '''read users and return result'''

@app.get("/users/{userId}", responses={404: {"model": OperationResult}})
async def read_user(userId:str) -> UserOut | None:
    '''read user and return result.
    use status code 404 if user is not found'''

@app.put('/users/{userId}')
async def update_user(userId:str,user:UserUpdate) -> OperationResult:
    ''' update user by id and return result'''

@app.delete('/users')
async def delete_users() -> OperationResult:
    '''reset DB and return result'''

@app.delete('/users/{userId}')
async def delete_user(userId:str) -> OperationResult:
    '''delete user by id'''
