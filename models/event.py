from uuid import uuid4
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Event(BaseModel):

    event_id: str = Field(default_factory=lambda: f"EVT-{uuid4().hex[:8].upper()}")

    timestamp: datetime

    event_code: Optional[int] = None

    event_type: str

    platform: str

    source: str

    severity: str = "Informational"

    username: Optional[str] = None

    hostname: Optional[str] = None

    source_ip: Optional[str] = None

    destination_ip: Optional[str] = None

    process: Optional[str] = None

    command: Optional[str] = None

    domain: Optional[str] = None

    url: Optional[str] = None

    file_hash: Optional[str] = None

    description: str = ""

    raw_data: str = ""

    evidence_id: Optional[str] = None

    parser: str = "Unknown"