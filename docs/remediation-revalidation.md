# Remediation and Revalidation Standard

Incident closure is a security decision, not an administrative ticket state. This lab separates containment, eradication, recovery, and revalidation so that a finding is not considered resolved until the intended control state is demonstrated with evidence.

## Closure states

| State | Meaning |
| --- | --- |
| `open` | Risk condition remains present or has not been addressed |
| `contained` | Immediate propagation or impact has been limited, but root cause may remain |
| `eradicated` | The identified persistence or control failure has been removed |
| `recovery_pending` | Service restoration is underway but post-change evidence is incomplete |
| `validated` | Required technical evidence confirms the intended control state |
| `exception` | Residual risk is explicitly accepted through a separate governance path |

Containment does not equal eradication. Eradication does not equal validated recovery. An exception does not reduce technical exposure; it records a governance decision about residual risk.

## Minimum closure evidence

A validated remediation record should contain:

1. **Accountable owner** — the team or role responsible for the change.
2. **Change reference** — a synthetic ticket/change identifier linking the control change to the finding.
3. **Implemented action** — what control was changed, removed, restored, or hardened.
4. **Scope confirmation** — affected host, identity, service, or control boundary checked after remediation.
5. **Post-change evidence** — telemetry or configuration evidence demonstrating the new state.
6. **Detection retest** — confirmation that the relevant detection/telemetry path still operates after the change.
7. **Recovery validation** — confirmation that business functionality and required security controls are both operating.
8. **Residual-risk statement** — any remaining uncertainty, dependency, exception, or monitoring requirement.

## Revalidation workflow

```text
Finding
  |
  v
Contain -> Preserve Evidence
  |
  v
Eradicate Root Cause / Control Failure
  |
  v
Restore Service or Identity State
  |
  v
Collect Post-change Evidence
  |
  +--> Control state wrong? --------> Reopen remediation
  |
  +--> Detection unavailable? -----> Reopen telemetry gap
  |
  +--> Business validation fails? -> Roll back / reassess
  |
  v
Validate Closure
```

## Scenario-specific examples

### Credential-access indicator

**Remediation objective:** remove the affected access path, reset or revoke synthetic identity state where applicable, and verify that credential-access telemetry remains available.

**Validation evidence:** no recurring synthetic indicator in the validation window, identity/session state reflects the intended change, and endpoint telemetry is healthy.

### Suspicious remote logon

**Remediation objective:** remove unauthorized access conditions and validate the intended administrative access boundary.

**Validation evidence:** expected source/identity restrictions are present, synthetic retest does not recreate the prior condition, and authentication logging is complete.

### Persistence indicator

**Remediation objective:** remove the persistence condition and address the control weakness that allowed it.

**Validation evidence:** persistence artifact absent from the synthetic post-change state, endpoint controls are healthy, and detection still identifies the equivalent synthetic behavior.

### Telemetry gap

**Remediation objective:** restore evidence visibility before relying on negative findings.

**Validation evidence:** expected endpoint or identity events are present, timestamps normalize correctly, and the assessment no longer reports the coverage gap.

## Exception governance

Risk acceptance is deliberately separate from remediation validation. An exception should identify an owner, approver, rationale, review reference, compensating controls, and expiry/review date. Expired or incomplete exceptions must not be treated as validated remediation.

## Safety boundary

All examples and references in this document are synthetic. The workflow describes defensive incident-response governance only; it does not automate production containment, account changes, host actions, credential handling, or destructive remediation.
