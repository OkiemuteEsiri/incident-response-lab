import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from src.engine import assess
from src.ingest import load_events
from src.models import EvidenceEvent, IncidentCase
from src.reporting import to_markdown


class IncidentResponseTests(unittest.TestCase):
    def setUp(self):
        self.case = IncidentCase("IR-1", "Synthetic", "high", "triage", datetime.now(timezone.utc), "SOC", True, "Portal", ("isolate_endpoint",))
        self.event = EvidenceEvent("E1", datetime.now(timezone.utc), "edr", "host1", "user1", "credential_access", "synthetic", 90)

    def test_credential_access_is_critical(self):
        result = assess(self.case, (self.event,))
        self.assertTrue(any(f.severity == "critical" for f in result.findings))

    def test_missing_identity_source_is_detected(self):
        result = assess(self.case, (self.event,))
        self.assertTrue(any(f.title == "Identity telemetry gap" for f in result.findings))

    def test_no_evidence_blocks_readiness(self):
        result = assess(self.case, ())
        self.assertFalse(result.containment_ready)

    def test_critical_asset_without_approval_not_ready(self):
        case = IncidentCase("IR-2", "Synthetic", "high", "triage", datetime.now(timezone.utc), "SOC", True, "Portal", ())
        result = assess(case, (self.event,))
        self.assertFalse(result.containment_ready)

    def test_noncritical_asset_can_be_ready(self):
        case = IncidentCase("IR-3", "Synthetic", "medium", "triage", datetime.now(timezone.utc), "SOC", False, "Lab", ())
        result = assess(case, (self.event,))
        self.assertTrue(result.containment_ready)

    def test_finding_ids_are_deterministic(self):
        a = assess(self.case, (self.event,))
        b = assess(self.case, (self.event,))
        self.assertEqual([f.finding_id for f in a.findings], [f.finding_id for f in b.findings])

    def test_risk_score_is_bounded(self):
        result = assess(self.case, (self.event, self.event))
        self.assertLessEqual(result.risk_score, 100)

    def test_duplicate_event_ids_fail_closed(self):
        rows = [{"event_id":"E1","timestamp":"2026-01-01T00:00:00Z","source":"edr","host":"h","user":"u","event_type":"x","summary":"s"}]*2
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "events.json"; p.write_text(json.dumps(rows), encoding="utf-8")
            with self.assertRaises(ValueError): load_events(p)

    def test_naive_timestamp_rejected(self):
        with self.assertRaises(ValueError):
            EvidenceEvent("E2", datetime(2026,1,1), "edr", "h", "u", "x", "s")

    def test_report_contains_attack_mapping(self):
        report = to_markdown(assess(self.case, (self.event,)))
        self.assertIn("T1003", report)
        self.assertIn("Risk score", report)


if __name__ == "__main__":
    unittest.main()
