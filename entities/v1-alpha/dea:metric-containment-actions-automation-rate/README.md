# dea:metric-containment-actions-automation-rate

Candidate Performance Metric record for **Containment Actions Automation Rate** (CAAR-SOC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-containment-actions-automation-rate`
- **Name:** Containment Actions Automation Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CAAR-SOC

## 2. Definition

Containment Actions Automation Rate (CAAR-SOC) addresses how efficiently resources are converted into outputs and is a fixture of secops & security operations center reporting. It is defined as Automated Containment Actions / Containment Actions; the result is stated in percent (%). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of standard containment actions (isolation, blocking, credential revocation) executed automatically by playbooks. Automated containment shrinks damage from minutes to seconds and frees analysts for investigation. Overly aggressive auto-containment can trigger self-denial incidents, so guardrails matter. Read with auto-remediation execution rate and mean time to contain - security.

## Formula

```
Automated Containment Actions / Containment Actions
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** secops_security_operations_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2783 (batch 7)
