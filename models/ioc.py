from uuid import uuid4
from datetime import datetime
from typing import List

from pydantic import BaseModel, Field, ConfigDict


class IOC(BaseModel):

    model_config = ConfigDict(
        validate_assignment=False,
        extra="ignore"
    )

    ioc_id: str = Field(
        default_factory=lambda: f"IOC-{uuid4().hex[:8].upper()}"
    )

    type: str

    value: str

    source: str = "Unknown"

    confidence: int = 100

    reputation: str = "Unknown"

    recommendation: str = "Monitor"

    first_seen: datetime = Field(
        default_factory=datetime.now
    )

    last_seen: datetime = Field(
        default_factory=datetime.now
    )

    related_events: List[str] = Field(
        default_factory=list
    )