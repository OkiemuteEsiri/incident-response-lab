# MITRE ATT&CK Mapping Guide

ATT&CK is used here as a defensive classification layer for synthetic evidence. A mapping means the observed behavior is relevant to a technique; it does not prove compromise, actor identity, campaign attribution, intent, or successful execution.

## Mapping matrix

| Technique | Defensive evidence context | Analyst interpretation | Validation / remediation focus |
| --- | --- | --- | --- |
| `T1003` OS Credential Dumping | Synthetic credential-access detection metadata | Potential credential-access activity requiring endpoint and identity correlation | Preserve evidence, validate endpoint telemetry, revoke affected synthetic sessions where justified, retest coverage |
| `T1021` Remote Services | Synthetic suspicious remote-logon evidence | Potential lateral or administrative remote access requiring source, identity, and authorization review | Validate access boundary, authentication logs, approved source path, and post-change retest |
| `T1078` Valid Accounts | Synthetic identity/authentication evidence | Legitimate credentials may be involved in suspicious activity; identity alone is not proof of compromise | Review session state, sign-in context, privilege, and authentication controls |
| `T1059.001` PowerShell | Synthetic PowerShell telemetry | Script interpreter activity requiring command context and adjacent evidence; PowerShell use alone is not malicious | Preserve command metadata, confirm business context, verify detection and logging coverage |
| `T1547` Boot or Logon Autostart Execution | Synthetic persistence metadata | Potential persistence condition requiring eradication and startup-path validation | Remove synthetic persistence state, address root control weakness, retest detection |
| `T1562.001` Impair Defenses | Synthetic evidence of degraded or missing defensive visibility | Potential defense impairment or telemetry loss; missing telemetry also reduces confidence in negative findings | Restore controls/telemetry, verify health, confirm expected event flow |

## Mapping confidence

The project separates three concepts:

- **Observed evidence** — the normalized synthetic event or control state.
- **ATT&CK relevance** — the technique whose behavior pattern best describes that evidence.
- **Incident conclusion** — the analyst decision made only after correlation, scope, confidence, and authorization review.

A single event may justify an ATT&CK mapping without justifying a compromise conclusion. Conversely, missing telemetry may increase response uncertainty even when it does not map cleanly to an adversary technique.

## Analyst use

ATT&CK context is intended to improve:

1. investigation consistency;
2. detection coverage review;
3. remediation traceability;
4. response handoff between endpoint, identity, network, and incident-command functions;
5. lessons-learned analysis after the synthetic scenario.

## Limitations

This repository does not implement actor attribution, intrusion-set matching, campaign clustering, threat-intelligence scoring, or live detection content deployment. ATT&CK mappings are intentionally conservative and should be reviewed against the exact evidence available in a real authorized environment.
