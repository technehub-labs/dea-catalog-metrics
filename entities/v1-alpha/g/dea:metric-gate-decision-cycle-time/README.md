# dea:metric-gate-decision-cycle-time

Candidate Performance Metric record for **Gate Decision Cycle Time** (GDCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-gate-decision-cycle-time`
- **Name:** Gate Decision Cycle Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** GDCT

## 2. Definition

Gate Decision Cycle Time (GDCT) captures how efficiently resources are converted into outputs for organizations tracking pmo & portfolio governance. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Days from Gate Submission to Decision, expressed in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
GDCT = Days from Gate Submission to Decision
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** governance
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** pmo_portfolio_governance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3412 (batch 7)
