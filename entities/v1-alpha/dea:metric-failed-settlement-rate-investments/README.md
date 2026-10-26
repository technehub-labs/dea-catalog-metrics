# dea:metric-failed-settlement-rate-investments

Candidate Performance Metric record for **Failed Settlement Rate (Investments)** (FSRI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-failed-settlement-rate-investments`
- **Name:** Failed Settlement Rate (Investments)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FSRI

## 2. Definition

Failed Settlement Rate (Investments) (FSRI) addresses the quality of outputs and outcomes and is a fixture of investment risk & middle office operations reporting. Its calculation is Settlements Failed on Settlement Date / Settlements, measured in percent (%). It originates from and is most used in Investment management practice. It provides the day-to-day signal that a process is running as designed. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Settlements Failed on Settlement Date / Settlements
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_risk_middle_office_operations
- **Sector:** investment_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3464 (batch 7)
