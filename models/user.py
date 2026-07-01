from uuid import uuid4
from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    user_id:str=Field(default_factory=lambda:f"USR-{uuid4().hex[:8].upper()}")
    name:str
    email:str
    role:str="SOC L1"
    team:str="Blue Team"
    phone:Optional[str]=None