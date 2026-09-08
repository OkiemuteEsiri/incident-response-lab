# Incident Response Lab

A defensive incident-response portfolio project that demonstrates structured triage, containment, evidence handling, timeline construction, eradication, recovery, and lessons learned.

## Scenario model
The lab uses synthetic events to represent a suspicious endpoint compromise. The focus is on analyst decision-making and evidence quality rather than offensive execution.

## Workflow

1. Validate the alert and establish incident scope.
2. Preserve volatile and durable evidence.
3. Build an event timeline.
4. Identify affected identities, hosts, and network paths.
5. Contain the incident with the least business disruption possible.
6. Eradicate persistence and remove malicious artifacts.
7. Recover systems and validate control effectiveness.
8. Produce lessons learned and detection improvements.

## Repository structure

- `playbooks/endpoint-compromise.md` — practical response playbook
- `templates/incident-timeline.csv` — synthetic timeline format
- `docs/evidence-handling.md` — evidence integrity and documentation guidance

## Skills demonstrated
Incident response, threat hunting, endpoint triage, evidence preservation, timeline analysis, containment strategy, stakeholder communication, and post-incident improvement.

## Safety
All examples are synthetic and intended for authorized defensive training. No real victim data, credentials, or malicious payloads are included.
