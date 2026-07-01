from uuid import uuid4
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from models.user import User
from models.asset import Asset
from models.evidence import Evidence
from models.event import Event
from models.ioc import IOC
from models.relationship import Relationship
from models.timeline import Timeline
from models.report import Report
from models.technique import Technique


class Incident(BaseModel):
    incident_id: str = Field(default_factory=lambda: f"INC-{uuid4().hex[:8].upper()}")

    title: str
    description: str = ""

    status: str = "Open"
    priority: str = "Medium"
    severity: str = "Medium"

    risk_score: int = 0

    assigned_analyst: Optional[User] = None

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    closed_at: Optional[datetime] = None

    evidence: List[Evidence] = Field(default_factory=list)
    events: List[Event] = Field(default_factory=list)
    iocs: List[IOC] = Field(default_factory=list)
    assets: List[Asset] = Field(default_factory=list)
    relationships: List[Relationship] = Field(default_factory=list)
    mitre_techniques: List[Technique] = Field(default_factory=list)

    timeline: Optional[Timeline] = None
    report: Optional[Report] = None

    analyst_notes: List[str] = Field(default_factory=list)