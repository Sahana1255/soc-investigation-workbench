from uuid import uuid4
from datetime import datetime
from pathlib import Path
from pydantic import BaseModel, Field

class Evidence(BaseModel):
    evidence_id:str=Field(default_factory=lambda:f"EVD-{uuid4().hex[:8].upper()}")
    filename:str
    filepath:Path
    file_type:str
    platform:str
    source:str="Upload"
    uploaded_at:datetime=Field(default_factory=datetime.now)
    file_size:int=0
    sha256:str=""
    parser_status:str="Pending"