from enum import Enum
from bson import ObjectId
from pydantic import BaseModel, Extra, Field
from typing import Optional

class User(BaseModel):
    id: str = Field(alias='_id',default=None)
    username:str
    password:str
    admin: Optional[bool] = False

class UserQuery(BaseModel):
    username: Optional[str] = None

class UserUpdate(BaseModel):
    password:Optional[str]=None