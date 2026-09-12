# Recruiter Review Guide

This repository is designed to be reviewed quickly without sacrificing technical depth. The implementation is defensive, deterministic, offline, and based entirely on synthetic incident data.

## Five-minute review path

1. Start with `README.md` for the problem statement, architecture, safety boundary, and operating model.
2. Read `src/engine.py` to see how normalized evidence becomes findings, ATT&CK context, risk, telemetry-gap analysis, and containment-readiness decisions.
3. Read `src/ingest.py` and `src/models.py` for fail-closed validation, UTC normalization, duplicate rejection, and immutable domain modeling.
4. Read `reports/example-assessment.md` for the analyst-facing output produced from the fictional incident scenario.
5. Read `tests/test_engine.py` and `.github/workflows/ci.yml` to see how deterministic behavior and report generation are validated.
6. Read `docs/remediation-revalidation.md` for the closure standard used after containment and eradication.

## Capability-to-evidence map

| Capability | Repository evidence | What it demonstrates |
| --- | --- | --- |
| Incident triage | `src/engine.py` | Structured correlation and prioritization from normalized evidence |
| Evidence quality | `src/ingest.py`, `src/models.py` | Fail-closed ingestion, duplicate rejection, explicit data contracts |
| Risk communication | `src/engine.py`, `src/reporting.py` | Explainable scoring and analyst-readable findings |
| Timeline analysis | `src/reporting.py` | Ordered incident chronology suitable for review and handoff |
| Containment governance | `src/engine.py`, `playbooks/endpoint-compromise.md` | Authorization-aware, least-disruptive containment decisioning |
| ATT&CK contextualization | `src/engine.py`, `docs/attack-mapping.md` | Defensive behavior mapping without attribution claims |
| Remediation validation | `docs/remediation-revalidation.md` | Evidence-based closure rather than ticket-based closure |
| Engineering quality | `tests/test_engine.py`, `.github/workflows/ci.yml` | Repeatable tests, compilation checks, deterministic output generation |

## Security engineering questions this project answers

- What evidence is sufficient to escalate an incident from observation to actionable finding?
- How should missing endpoint or identity telemetry affect confidence and containment readiness?
- How can a response workflow remain deterministic while preserving analyst judgment and authorization boundaries?
- How should a critical business service influence containment decisions without suppressing security risk?
- What evidence is required before declaring remediation complete?
- How should ATT&CK mappings be used as behavior context without over-claiming compromise or actor attribution?

## Recruiter signal

The strongest signal is not repository size. It is the combination of defensive decision logic, explicit trust boundaries, deterministic identifiers, validation gates, synthetic evidence, technical documentation, tests, and clear limitations. The repository intentionally does not perform live containment, credential handling, exploitation, malware execution, host acquisition, or production targeting.

## Verification note

A historical green workflow does not prove the current commit is green. GitHub Actions status should be checked against the exact commit under review before making a CI claim.
