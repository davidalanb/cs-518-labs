from pydantic import BaseModel, Extra, Field
from typing import Optional

class Address(BaseModel):
    line1:str
    line2:Optional[str]=None
    city:str
    state:str
    zip:str

class UserIn(BaseModel):
    username:str
    password:str
    address:Optional[Address] = None

class UserOut(BaseModel):
    id: str = Field(alias='_id')
    username: str
    password: str
    address:Optional[Address] = None

class UserQuery(BaseModel):
    username: str

class UserUpdate(BaseModel):
    password:Optional[str]=None
    address:Optional[Address]=None

class UserCollection(BaseModel):
    users: list[UserOut]

class OperationResult(BaseModel):
    status: int
    message: Optional[str]=None
    
class CreateUserResult(OperationResult):
    inserted_id: Optional[str] = None

class UpdateUserResult(OperationResult):
    modified_count: Optional[int] = None