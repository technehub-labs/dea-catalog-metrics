# dea:metric-penetration-test-finding-recurrence-rate

Candidate Performance Metric record for **Penetration Test Finding Recurrence Rate** (PTFRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-penetration-test-finding-recurrence-rate`
- **Name:** Penetration Test Finding Recurrence Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PTFRR

## 2. Definition

A DevSecOps & Application Security Engineering indicator, Penetration Test Finding Recurrence Rate (PTFRR) quantifies exposure to adverse outcomes. It is defined as Findings Recurring from Prior Test / Findings; the result is stated in percent (%). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the share of pen-test findings that reappear in later engagements. Recurrence proves that root causes are being patched cosmetically rather than fixed structurally. Low recurrence requires disciplined remediation plus verification testing, not just closing tickets. Read with DAST coverage of attack surface and threat modeling coverage for new services.

## Formula

```
PTFRR = Findings Recurring from Prior Test / Findings
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** devsecops_application_security_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2766 (batch 7)
