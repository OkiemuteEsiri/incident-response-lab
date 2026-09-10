# Incident Response Lab

A defensive, recruiter-facing incident-response engineering project that demonstrates structured triage, evidence handling, containment decisioning, eradication, recovery validation, ATT&CK contextualization, repeatable reporting, and CI-tested security logic using synthetic data only.

## Problem Statement
Incident response programs fail when evidence is incomplete, timelines are inconsistent, containment is disruptive or unauthorized, and remediation is closed without validation. This project models a disciplined response pipeline that converts normalized evidence into deterministic findings, an explainable risk score, containment-readiness decisions, and an auditable report.

## Architecture

```text
Synthetic Case + Evidence JSON
          |
          v
 Fail-Closed Ingestion
          |
          v
 Immutable Domain Models
          |
          v
 Assessment / Correlation Engine
   |         |          |
   |         |          +--> ATT&CK context
   |         +-------------> telemetry-gap checks
   +-----------------------> containment-readiness gate
          |
          v
 Risk Score + Findings + Timeline
          |
          v
 Markdown Report / Analyst CLI
```

### Core Modules
- `src/models.py` — validated immutable case, evidence, finding, and assessment objects.
- `src/ingest.py` — required-field validation, UTC normalization, duplicate-event rejection, fail-closed loading.
- `src/engine.py` — deterministic triage, telemetry-gap analysis, ATT&CK mappings, risk scoring, and containment readiness.
- `src/reporting.py` — recruiter-readable findings and normalized incident timeline generation.
- `src/cli.py` — offline analyst workflow for repeatable synthetic assessments.
- `tests/test_engine.py` — meaningful tests for validation, deterministic IDs, scoring, safety gates, ingestion, and reporting.

## Incident Workflow
1. **Preparation** — confirm ownership, logging, escalation paths, containment authority, rollback criteria, and business criticality.
2. **Detection & Triage** — validate alert fidelity and correlate endpoint, identity, authentication, and network evidence.
3. **Scope** — identify affected hosts, users, services, indicators, and adjacent attack paths.
4. **Containment** — select the least disruptive approved action that stops further harm while preserving evidence.
5. **Eradication** — remove persistence, revoke affected sessions, address root control failures, and document changes.
6. **Recovery** — restore service only after control and telemetry validation.
7. **Lessons Learned** — capture root cause, detection gaps, response friction, remediation ownership, and measurable improvements.

## Defensive Detection Logic
The current engine identifies:
- missing endpoint telemetry;
- missing identity/authentication telemetry;
- synthetic credential-access indicators;
- suspicious remote-logon activity;
- persistence indicators requiring eradication;
- containment-authority gaps for critical business assets.

Risk is intentionally simple and explainable: low=8, medium=15, high=25, critical=40, capped at 100. A score never substitutes for incident-commander judgment or containment authorization.

## MITRE ATT&CK Context
Relevant defensive mappings include:
- `T1003` — OS Credential Dumping
- `T1021` — Remote Services
- `T1078` — Valid Accounts
- `T1059.001` — PowerShell
- `T1547` — Boot or Logon Autostart Execution
- `T1562.001` — Impair Defenses

Mappings describe synthetic observed behavior and do not imply actor attribution.

## Usage

```bash
python -m src.cli \
  --case data/synthetic-case.json \
  --events data/synthetic-events.json \
  --output reports/generated-assessment.md
```

Run the unit tests:

```bash
python -m unittest discover -s tests -v
```

No third-party Python dependency is required.

## Synthetic Scenario
The included fixture models a suspicious endpoint-and-identity incident affecting a fictional finance portal. Evidence includes synthetic identity, PowerShell telemetry, credential-access detection metadata, and persistence metadata. No credential material, malware, exploit code, production identifiers, or real victim data is present.

## Remediation and Validation
Findings are designed to drive measurable follow-up. Examples include acquiring missing telemetry, revoking synthetic sessions, validating identity containment, removing persistence indicators, retesting detection coverage, and collecting post-change evidence. A remediation is not considered complete solely because a ticket is closed; validation evidence must demonstrate the intended control state.

## CI/CD Security Checks
`.github/workflows/ci.yml` uses least-privilege `contents: read` permissions and performs:
- Python compilation;
- unit-test discovery;
- deterministic generation of the synthetic assessment report.

CI status must be checked in GitHub before claiming these checks passed.

## Repository Structure

```text
.github/workflows/ci.yml
data/
  synthetic-case.json
  synthetic-events.json
docs/
  architecture.md
  methodology.md
playbooks/
  endpoint-compromise.md
reports/
  example-assessment.md
src/
  __init__.py
  cli.py
  engine.py
  ingest.py
  models.py
  reporting.py
tests/
  test_engine.py
README.md
```

## Design Principles
- Evidence-first and deterministic decision logic.
- Fail-closed ingestion rather than silent data acceptance.
- Explicit separation between evidence, analyst inference, and authorization.
- Least-disruptive containment for critical services.
- Stable finding IDs for remediation lifecycle tracking.
- Offline execution and synthetic-only evidence.
- Clear limitations and no unsupported attribution claims.

## Skills Demonstrated
Incident response engineering, SOC triage, endpoint and identity analysis, evidence normalization, timeline analysis, risk communication, ATT&CK mapping, deterministic Python design, defensive automation, remediation validation, technical documentation, unit testing, and secure CI/CD design.

## Limitations
This is a portfolio lab, not a replacement for EDR, SIEM, SOAR, forensic acquisition, malware analysis, or incident-command platforms. The scoring model is intentionally transparent rather than statistically predictive. It does not perform live containment, host acquisition, network scanning, credential handling, exploitation, or production actions.

## Roadmap
- Add evidence provenance and chain-of-custody metadata.
- Add host/user/entity relationship correlation.
- Add configurable severity and containment policies.
- Add Sigma-style detection metadata validation.
- Add structured lessons-learned and remediation SLA tracking.
- Add machine-readable JSON report export.
- Add richer scenario packs for cloud, identity, ransomware-prevention, and insider-risk exercises.

## Safety
All examples are synthetic and intended for authorized defensive training. The repository contains no real credentials, employer/client data, exploit payloads, malware, persistence tooling, command-and-control infrastructure, or live production targeting.
