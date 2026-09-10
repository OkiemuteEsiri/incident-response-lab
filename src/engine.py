import hashlib
from collections import Counter
from .models import Assessment, EvidenceEvent, Finding, IncidentCase

ATTACK = {
    "credential_access": ("T1003",),
    "remote_logon": ("T1021", "T1078"),
    "powershell": ("T1059.001",),
    "persistence": ("T1547",),
    "defense_evasion": ("T1562.001",),
}


def _finding(case_id: str, title: str, severity: str, rationale: str, remediation: str, attack_ids=()) -> Finding:
    digest = hashlib.sha256(f"{case_id}|{title}|{rationale}".encode()).hexdigest()[:12]
    return Finding(f"IR-{digest}", title, severity, rationale, remediation, tuple(attack_ids))


def assess(case: IncidentCase, events: tuple[EvidenceEvent, ...]) -> Assessment:
    findings = []
    types = Counter(e.event_type for e in events)
    sources = {e.source.lower() for e in events}

    if not events:
        findings.append(_finding(case.case_id, "No evidence available", "critical", "No event evidence was supplied for triage.", "Acquire and preserve endpoint, identity, network and authentication evidence before containment decisions."))
    if "edr" not in sources:
        findings.append(_finding(case.case_id, "Endpoint telemetry gap", "high", "No EDR evidence is present.", "Acquire endpoint telemetry or document an approved alternative evidence source."))
    if "identity" not in sources:
        findings.append(_finding(case.case_id, "Identity telemetry gap", "high", "No identity provider or authentication evidence is present.", "Acquire authentication and identity telemetry and correlate affected accounts."))
    if "credential_access" in types:
        findings.append(_finding(case.case_id, "Credential-access indicators observed", "critical", f"{types['credential_access']} synthetic credential-access event(s) require identity containment.", "Reset or revoke affected synthetic identities in the exercise plan and validate session/token invalidation.", ATTACK["credential_access"]))
    if "remote_logon" in types:
        findings.append(_finding(case.case_id, "Suspicious remote logon activity", "high", f"{types['remote_logon']} remote-logon event(s) expand possible incident scope.", "Validate source/destination pairs, affected identities, approved administration paths, and lateral-movement controls.", ATTACK["remote_logon"]))
    if "persistence" in types:
        findings.append(_finding(case.case_id, "Persistence indicator requires eradication", "high", "Synthetic persistence telemetry exists and must be removed before recovery.", "Document eradication action, collect post-change evidence, and re-run persistence-focused detection checks.", ATTACK["persistence"]))
    if case.critical_asset and not case.approved_containment:
        findings.append(_finding(case.case_id, "Critical-asset containment not pre-authorized", "high", "The affected asset supports a critical business service and has no approved containment actions.", "Establish an approved containment decision with business owner, incident commander, and rollback conditions."))

    weights = {"low": 8, "medium": 15, "high": 25, "critical": 40}
    score = min(100, sum(weights[f.severity] for f in findings))
    containment_ready = bool(events) and not any(f.severity == "critical" and f.title == "No evidence available" for f in findings) and (not case.critical_asset or bool(case.approved_containment))
    return Assessment(case, events, tuple(findings), score, containment_ready)
