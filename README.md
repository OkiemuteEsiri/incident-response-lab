# Incident Response Lab

A defensive, recruiter-facing incident-response engineering project that demonstrates structured triage, evidence handling, containment decisioning, eradication, recovery validation, ATT&CK contextualization, repeatable reporting, and CI-tested security logic using synthetic data only.

## Recruiter Quick Review

For a focused technical review, use this sequence:

1. **Architecture and operating model:** this README plus [`docs/architecture.md`](docs/architecture.md).
2. **Decision logic:** [`src/engine.py`](src/engine.py) for findings, risk scoring, telemetry gaps, ATT&CK context, and containment readiness.
3. **Evidence quality:** [`src/ingest.py`](src/ingest.py) and [`src/models.py`](src/models.py) for validation, UTC normalization, duplicate rejection, and domain contracts.
4. **Analyst output:** [`reports/example-assessment.md`](reports/example-assessment.md).
5. **Closure standard:** [`docs/remediation-revalidation.md`](docs/remediation-revalidation.md).
6. **ATT&CK interpretation:** [`docs/attack-mapping.md`](docs/attack-mapping.md).
7. **Tests and CI:** [`tests/test_engine.py`](tests/test_engine.py) and [`.github/workflows/ci.yml`](.github/workflows/ci.yml).

See [`docs/recruiter-review.md`](docs/recruiter-review.md) for the full capability-to-evidence map.

### Recruiter Signal at a Glance

| Capability | Evidence |
| --- | --- |
| Incident triage and correlation | Deterministic assessment engine over normalized synthetic endpoint/identity evidence |
| Evidence integrity | Fail-closed validation, duplicate rejection, immutable models, UTC normalization |
| Risk communication | Explainable bounded scoring, stable finding identifiers, analyst-readable reporting |
| Containment governance | Authorization-aware readiness checks and least-disruptive response framing |
| ATT&CK contextualization | Conservative defensive mappings separated from attribution and compromise claims |
| Remediation assurance | Explicit containment → eradication → recovery → revalidation lifecycle |
| Engineering quality | Unit tests, compilation checks, deterministic report generation, least-privilege CI |

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

Mappings describe synthetic observed behavior and do not imply actor attribution, intent, successful execution, or confirmed compromise. The mapping methodology and analyst interpretation boundaries are documented in [`docs/attack-mapping.md`](docs/attack-mapping.md).

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

## Remediation and Revalidation
Findings are designed to drive measurable follow-up. A remediation is not considered complete solely because a ticket is closed. This project separates:

- **containment** — immediate risk reduction;
- **eradication** — removal of persistence or the underlying control failure;
- **recovery** — restoration of required business functionality and security controls;
- **revalidation** — post-change evidence proving the intended control state;
- **exception governance** — explicit acceptance of residual risk, separate from technical remediation state.

The minimum closure evidence and scenario-specific validation workflow are documented in [`docs/remediation-revalidation.md`](docs/remediation-revalidation.md).

## CI/CD Security Checks
`.github/workflows/ci.yml` uses least-privilege `contents: read` permissions and performs:
- Python compilation;
- unit-test discovery;
- deterministic generation of the synthetic assessment report.

CI status must be checked against the **exact commit under review** before claiming these checks passed. A historical green run is not treated as evidence for a later commit.

## Repository Structure

```text
.github/workflows/ci.yml
data/
  synthetic-case.json
  synthetic-events.json
docs/
  architecture.md
  attack-mapping.md
  methodology.md
  recruiter-review.md
  remediation-revalidation.md
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
- Technical remediation state is separate from exception/risk-acceptance state.
- Offline execution and synthetic-only evidence.
- Clear limitations and no unsupported attribution claims.

## Skills Demonstrated
Incident response engineering, SOC triage, endpoint and identity analysis, evidence normalization, timeline analysis, risk communication, ATT&CK mapping, deterministic Python design, defensive automation, remediation validation, technical documentation, unit testing, and secure CI/CD design.

## Limitations
This is a portfolio lab, not a replacement for EDR, SIEM, SOAR, forensic acquisition, malware analysis, or incident-command platforms. The scoring model is intentionally transparent rather than statistically predictive. It does not perform live containment, host acquisition, network scanning, credential handling, exploitation, production actions, actor attribution, or destructive remediation.

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
