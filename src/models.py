from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Tuple

VALID_SEVERITIES = {"low", "medium", "high", "critical"}
VALID_STATES = {"new", "triage", "contained", "eradicated", "recovered", "closed"}


def parse_utc(value: str) -> datetime:
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        raise ValueError("timestamps must include timezone information")
    return dt.astimezone(timezone.utc)


@dataclass(frozen=True)
class EvidenceEvent:
    event_id: str
    timestamp: datetime
    source: str
    host: str
    user: str
    event_type: str
    summary: str
    confidence: int = 50
    indicators: Tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        if not self.event_id.strip():
            raise ValueError("event_id is required")
        if not 0 <= self.confidence <= 100:
            raise ValueError("confidence must be between 0 and 100")
        if self.timestamp.tzinfo is None:
            raise ValueError("timestamp must be timezone-aware")


@dataclass(frozen=True)
class IncidentCase:
    case_id: str
    title: str
    severity: str
    state: str
    opened_at: datetime
    owner: str
    critical_asset: bool
    business_service: str
    approved_containment: Tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        if self.severity not in VALID_SEVERITIES:
            raise ValueError(f"invalid severity: {self.severity}")
        if self.state not in VALID_STATES:
            raise ValueError(f"invalid state: {self.state}")
        if not self.case_id.strip() or not self.owner.strip():
            raise ValueError("case_id and owner are required")


@dataclass(frozen=True)
class Finding:
    finding_id: str
    title: str
    severity: str
    rationale: str
    remediation: str
    attack_ids: Tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class Assessment:
    case: IncidentCase
    events: Tuple[EvidenceEvent, ...]
    findings: Tuple[Finding, ...]
    risk_score: int
    containment_ready: bool
