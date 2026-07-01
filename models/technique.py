from uuid import uuid4
from typing import List
from pydantic import BaseModel, Field


class Technique(BaseModel):
    technique_id:str=Field(default_factory=lambda:f"TEC-{uuid4().hex[:8].upper()}")

    framework:str="MITRE ATT&CK"

    tactic:str

    technique:str

    description:str=""

    confidence:int=100

    related_events:List[str]=Field(default_factory=list)