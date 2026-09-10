# Incident Response Methodology

## Lifecycle
1. **Preparation** — establish ownership, evidence sources, containment authorities, communication paths, and rollback criteria.
2. **Detection & Triage** — validate alert fidelity, correlate endpoint/identity/network evidence, classify severity, and identify initial scope.
3. **Containment** — use the least disruptive approved action that stops further harm while preserving evidence.
4. **Eradication** — remove persistence, revoke compromised sessions, correct exposed credentials, and close exploited control gaps.
5. **Recovery** — restore business service, validate endpoint and identity health, monitor for recurrence, and confirm control effectiveness.
6. **Lessons Learned** — document root cause, detection gaps, timeline, response friction, remediation ownership, and measurable follow-up actions.

## Evidence Quality Controls
- Require timezone-aware timestamps.
- Reject duplicate event IDs.
- Record source, host, user, event type, summary, confidence, and indicators.
- Distinguish observed evidence from analyst inference.
- Preserve synthetic evidence immutably once ingested into the assessment.

## Containment Decision Model
Critical assets require pre-approved containment actions. A high risk score does not automatically authorize disruptive containment. Analysts must combine evidence, scope, business criticality, and explicit authority.

## Remediation Validation
A remediation is not considered complete until post-change evidence demonstrates the intended control state. Validation examples include successful session revocation, clean endpoint telemetry, absence of persistence indicators, restored logging coverage, and repeat detection tests.

## ATT&CK Context
The project maps observed synthetic behaviors to ATT&CK where relevant: T1003 Credential Dumping, T1021 Remote Services, T1078 Valid Accounts, T1059.001 PowerShell, T1547 Boot or Logon Autostart Execution, and T1562.001 Impair Defenses. Mapping is contextual and does not imply confirmed adversary attribution.
