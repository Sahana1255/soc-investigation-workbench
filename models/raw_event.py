from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class RawEvent(BaseModel):

    timestamp: datetime

    platform: str

    source: str

    event_type: str

    event_code: Optional[str] = None

    severity: str = "Informational"

    username: Optional[str] = None

    hostname: Optional[str] = None

    process: Optional[str] = None

    command: Optional[str] = None

    source_ip: Optional[str] = None

    destination_ip: Optional[str] = None

    url: Optional[str] = None

    domain: Optional[str] = None

    file_hash: Optional[str] = None

    description: str = ""

    raw_data: str = ""