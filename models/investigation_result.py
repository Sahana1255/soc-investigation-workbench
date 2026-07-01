from uuid import uuid4
from typing import List

from pydantic import BaseModel, Field

from models.event import Event
from models.ioc import IOC
from models.asset import Asset
from models.technique import Technique


class InvestigationResult(BaseModel):

    investigation_id: str = Field(
        default_factory=lambda: f"INV-{uuid4().hex[:8].upper()}"
    )

    event: Event

    iocs: List[IOC] = Field(default_factory=list)

    users: List[str] = Field(default_factory=list)

    assets: List[Asset] = Field(default_factory=list)

    processes: List[str] = Field(default_factory=list)

    network: List[str] = Field(default_factory=list)

    techniques: List[Technique] = Field(default_factory=list)

    alerts: List[dict] = Field(default_factory=list)

    risk_score: int = 0

    severity: str = "Low"