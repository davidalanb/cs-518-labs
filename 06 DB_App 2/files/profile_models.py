from datetime import datetime
from typing import List, Optional, Tuple
from pydantic import BaseModel, Field

# PROFILES

class Profile(BaseModel):
    id: str = Field(alias='_id',default=None)
    user_id: str
    profile_name: str
    skills: Optional[List[str]] = []

class ProfileCollection(BaseModel):
    profiles:List[Profile]

class ProfileQuery(BaseModel):
    user_id: Optional[str]=None

class ProfileUpdate(BaseModel):
    skills: Optional[List[str]] = []

    