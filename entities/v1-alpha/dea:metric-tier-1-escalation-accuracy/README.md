# dea:metric-tier-1-escalation-accuracy

Candidate Performance Metric record for **Tier-1 Escalation Accuracy** (T1EA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-tier-1-escalation-accuracy`
- **Name:** Tier-1 Escalation Accuracy
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** T1EA

## 2. Definition

Tier-1 Escalation Accuracy (T1EA) addresses the quality of outputs and outcomes and is a fixture of secops & security operations center reporting. It is computed as Escalations Justified / Escalations, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Escalations Justified / Escalations
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** secops_security_operations_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2779 (batch 7)
