from uuid import uuid4
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field


class Timeline(BaseModel):
    timeline_id:str=Field(default_factory=lambda:f"TML-{uuid4().hex[:8].upper()}")

    incident_id:str

    events:List[str]=Field(default_factory=list)

    start_time:datetime=Field(default_factory=datetime.now)

    end_time:datetime=Field(default_factory=datetime.now)

    summary:str=""