from uuid import uuid4
from pydantic import BaseModel, Field
from typing import Optional

class Asset(BaseModel):
    asset_id:str=Field(default_factory=lambda:f"AST-{uuid4().hex[:8].upper()}")
    hostname:str
    ip:str
    operating_system:str
    owner:Optional[str]=None
    criticality:str="Medium"
    status:str="Active"