# dea:metric-reconciliation-break-rate-positions

Candidate Performance Metric record for **Reconciliation Break Rate (Positions)** (RBRP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-reconciliation-break-rate-positions`
- **Name:** Reconciliation Break Rate (Positions)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RBRP

## 2. Definition

Reconciliation Break Rate (Positions) (RBRP) captures the quality of outputs and outcomes for organizations tracking investment risk & middle office operations. Its calculation is Unreconciled Position Breaks / Positions Reconciled, measured in events per thousand or million (scaled). It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. It originates from and is most used in Investment management practice.

## Formula

```
Unreconciled Position Breaks / Positions Reconciled
```

## Unit

- **Unit reference:** `dea:unit-events`
- **Unit:** events
- **Unit label (as published):** events per thousand or million (scaled)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3465 (batch 7)
