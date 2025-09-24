from datetime import datetime
from typing import List, Optional, Tuple
from pydantic import BaseModel, Field

class Adventure(BaseModel):
    id: str = Field(alias='_id',default=None)

    # profile used to create the adventure
    profile_id:str

    # essentials
    name: str
    datetime: datetime
    location: Optional[Tuple[float, float]] = None
    description: Optional[str] = None    
    skills: Optional[List[str]] = []
    
    # lists of profile_ids
    guides: Optional[List[str]] = []
    adventurers: Optional[List[str]] = []

class AdventureCollection(BaseModel):
    adventures: List[Adventure]

class AdventureQuery(BaseModel):
   user_id: Optional[str] = None

    