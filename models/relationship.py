from uuid import uuid4
from pydantic import BaseModel, Field


class Relationship(BaseModel):
    relationship_id:str=Field(default_factory=lambda:f"REL-{uuid4().hex[:8].upper()}")

    source:str
    target:str

    relationship_type:str

    confidence:int=100

    description:str=""