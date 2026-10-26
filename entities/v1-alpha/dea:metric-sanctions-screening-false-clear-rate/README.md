# dea:metric-sanctions-screening-false-clear-rate

Candidate Performance Metric record for **Sanctions Screening False Clear Rate** (SSFCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-sanctions-screening-false-clear-rate`
- **Name:** Sanctions Screening False Clear Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SSFCR

## 2. Definition

Sanctions Screening False Clear Rate (SSFCR) addresses the quality of outputs and outcomes and is a fixture of enterprise fraud & financial crime management reporting. It is computed as Cleared Alerts Reversed on Review / Alerts Cleared, expressed in events per thousand or million (scaled). It is applied across virtually every sector. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Cleared Alerts Reversed on Review / Alerts Cleared
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** risk
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** enterprise_fraud_financial_crime_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3772 (batch 8)
