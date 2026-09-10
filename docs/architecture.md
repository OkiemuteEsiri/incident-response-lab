# Architecture

## Purpose
This project models a defensive incident-response workflow using synthetic evidence. It is intentionally offline and separates evidence ingestion, domain validation, assessment logic, reporting, and operator interaction.

## Components

1. `src/models.py` — immutable case, evidence, finding, and assessment objects with validation.
2. `src/ingest.py` — fail-closed JSON parsing, required-field checks, duplicate-event rejection, and UTC normalization.
3. `src/engine.py` — deterministic triage logic, telemetry-gap checks, ATT&CK contextualization, containment-readiness evaluation, and risk scoring.
4. `src/reporting.py` — human-readable Markdown assessment and normalized timeline output.
5. `src/cli.py` — offline analyst interface suitable for repeatable portfolio demonstrations.
6. `data/` — synthetic case and evidence fixtures only.
7. `tests/` — unit tests for validation, scoring, deterministic IDs, safety gates, and reporting.

## Data Flow

`synthetic JSON -> fail-closed ingestion -> immutable domain objects -> deterministic assessment -> findings + readiness decision -> Markdown report`

## Design Principles

- Evidence first: decisions are derived from supplied evidence rather than unsupported assumptions.
- Fail closed: malformed or ambiguous records raise errors instead of being silently accepted.
- Deterministic output: the same case and evidence generate stable finding identifiers.
- Least disruptive containment: critical business assets require explicitly approved containment actions.
- Separation of concern: telemetry acquisition, assessment, containment authorization, eradication, and recovery remain distinct stages.
- Safe by design: the repository contains no malware, exploit code, real credentials, live containment actions, or production targeting.

## Risk Model

Finding weights are intentionally simple and explainable: low=8, medium=15, high=25, critical=40, capped at 100. The score is a prioritization aid rather than a substitute for incident commander judgment.
