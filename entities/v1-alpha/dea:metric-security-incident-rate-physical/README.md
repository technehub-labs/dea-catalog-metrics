# dea:metric-security-incident-rate-physical

Candidate Performance Metric record for **Security Incident Rate (Physical)** (SIRP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-security-incident-rate-physical`
- **Name:** Security Incident Rate (Physical)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SIRP

## 2. Definition

Within Physical Security Operations, Security Incident Rate (Physical) (SIRP) is used to gauge exposure to adverse outcomes. It is defined as Security Incidents per Site per Period; the result is stated in ratio (x:1 or x). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Security incident rate measures security-relevant events per site or per period - thefts, assaults, disturbances, access violations - and it is the effectiveness-visible metric of physical security operations. Its measurement honesty is the reporting paradox: better security programs surface more incidents (reporting channels, trust in response) while failing programs suppress them, so a rising rate can mean improving detection rather than deteriorating security - the interpretation depends on severity mix and resolution. The escalation taxonomy matters: minor incidents handled at first contact versus events requiring police engagement carry different cost and risk. Read with incident severity distribution, response-time performance, and the leading-indicator pair of access-control anomalies and officer patrol compliance, plus near-miss reporting which is the true prevention signal.

## Formula

```
Security Incidents per Site per Period
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** physical_security_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1208 (batch 4)
