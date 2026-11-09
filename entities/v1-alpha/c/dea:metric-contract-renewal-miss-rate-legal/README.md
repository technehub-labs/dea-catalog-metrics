# dea:metric-contract-renewal-miss-rate-legal

Candidate Performance Metric record for **Contract Renewal Miss Rate (Legal)** (CRML) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-contract-renewal-miss-rate-legal`
- **Name:** Contract Renewal Miss Rate (Legal)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CRML

## 2. Definition

A Legal Operations indicator, Contract Renewal Miss Rate (Legal) (CRML) quantifies exposure to adverse outcomes. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Renewals Lapsed without Action / Renewals Due, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
CRML = Renewals Lapsed without Action / Renewals Due
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** legal_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1683 (batch 6)
