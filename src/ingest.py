import json
from pathlib import Path
from .models import EvidenceEvent, IncidentCase, parse_utc

REQUIRED_CASE = {"case_id", "title", "severity", "state", "opened_at", "owner", "critical_asset", "business_service"}
REQUIRED_EVENT = {"event_id", "timestamp", "source", "host", "user", "event_type", "summary"}


def _require(record: dict, required: set[str], label: str) -> None:
    missing = sorted(required - set(record))
    if missing:
        raise ValueError(f"{label} missing required fields: {', '.join(missing)}")


def load_case(path: str | Path) -> IncidentCase:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    _require(data, REQUIRED_CASE, "case")
    return IncidentCase(
        case_id=str(data["case_id"]),
        title=str(data["title"]),
        severity=str(data["severity"]).lower(),
        state=str(data["state"]).lower(),
        opened_at=parse_utc(str(data["opened_at"])),
        owner=str(data["owner"]),
        critical_asset=bool(data["critical_asset"]),
        business_service=str(data["business_service"]),
        approved_containment=tuple(data.get("approved_containment", [])),
    )


def load_events(path: str | Path) -> tuple[EvidenceEvent, ...]:
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        raise ValueError("event evidence must be a JSON array")
    events = []
    seen = set()
    for row in raw:
        _require(row, REQUIRED_EVENT, "event")
        event_id = str(row["event_id"])
        if event_id in seen:
            raise ValueError(f"duplicate event_id: {event_id}")
        seen.add(event_id)
        events.append(EvidenceEvent(
            event_id=event_id,
            timestamp=parse_utc(str(row["timestamp"])),
            source=str(row["source"]),
            host=str(row["host"]),
            user=str(row["user"]),
            event_type=str(row["event_type"]),
            summary=str(row["summary"]),
            confidence=int(row.get("confidence", 50)),
            indicators=tuple(row.get("indicators", [])),
        ))
    return tuple(sorted(events, key=lambda e: e.timestamp))
