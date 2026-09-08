# Endpoint Compromise Response Playbook

## Trigger conditions
Use this playbook when endpoint telemetry indicates suspicious process execution, credential misuse, persistence, lateral movement, or confirmed malicious activity.

## Triage
- Confirm host identity, owner, business function, and criticality.
- Capture alert context, process tree, user context, network connections, hashes, and timestamps.
- Check for related alerts on the same identity or peer systems.
- Record all actions in the incident timeline.

## Containment
Choose the least disruptive effective control. Options can include endpoint isolation, account restriction, blocking confirmed indicators, or temporary network controls. Coordinate containment where systems are safety-critical or business-critical.

## Investigation
- Review process execution and parent/child relationships.
- Examine authentication activity and privilege changes.
- Review persistence locations and scheduled execution.
- Correlate DNS, proxy, firewall, EDR, and identity telemetry.
- Determine initial access, scope, and affected assets.

## Eradication and recovery
Remove confirmed malicious artifacts, rotate exposed credentials, correct exploited configuration weaknesses, patch relevant vulnerabilities, restore known-good state, and monitor for recurrence.

## Closure criteria
The incident may close when scope is understood, persistence is removed, affected credentials are remediated, recovery is validated, monitoring shows no recurrence, and lessons learned are captured.
