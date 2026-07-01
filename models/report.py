from uuid import uuid4
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class Report(BaseModel):
    report_id:str=Field(default_factory=lambda:f"RPT-{uuid4().hex[:8].upper()}")

    incident_id:str

    executive_summary:str=""

    technical_summary:str=""

    recommendations:str=""

    created_at:datetime=Field(default_factory=datetime.now)

    author:Optional[str]=None