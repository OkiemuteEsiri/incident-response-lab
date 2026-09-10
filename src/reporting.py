from .models import Assessment


def to_markdown(assessment: Assessment) -> str:
    c = assessment.case
    lines = [
        f"# Incident Assessment: {c.case_id}",
        "",
        f"**Title:** {c.title}",
        f"**Severity:** {c.severity.upper()}",
        f"**State:** {c.state}",
        f"**Owner:** {c.owner}",
        f"**Business service:** {c.business_service}",
        f"**Risk score:** {assessment.risk_score}/100",
        f"**Containment ready:** {'Yes' if assessment.containment_ready else 'No'}",
        "",
        "## Evidence Summary",
        f"- Events: {len(assessment.events)}",
        f"- Sources: {', '.join(sorted({e.source for e in assessment.events})) or 'none'}",
        f"- Hosts: {', '.join(sorted({e.host for e in assessment.events})) or 'none'}",
        f"- Users: {', '.join(sorted({e.user for e in assessment.events})) or 'none'}",
        "",
        "## Findings",
    ]
    if not assessment.findings:
        lines.append("No findings identified in the supplied synthetic evidence.")
    for f in assessment.findings:
        lines.extend([
            f"### {f.severity.upper()} — {f.title}",
            f"- Finding ID: `{f.finding_id}`",
            f"- Rationale: {f.rationale}",
            f"- Remediation: {f.remediation}",
            f"- MITRE ATT&CK: {', '.join(f.attack_ids) if f.attack_ids else 'N/A'}",
            "",
        ])
    lines.extend(["## Timeline", "| Timestamp (UTC) | Source | Host | User | Event | Summary |", "|---|---|---|---|---|---|"])
    for e in assessment.events:
        lines.append(f"| {e.timestamp.isoformat()} | {e.source} | {e.host} | {e.user} | {e.event_type} | {e.summary} |")
    return "\n".join(lines) + "\n"
