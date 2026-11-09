# dea:metric-data-access-request-fulfilment-time

Candidate Performance Metric record for **Data Access Request Fulfilment Time** (DARFT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-access-request-fulfilment-time`
- **Name:** Data Access Request Fulfilment Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DARFT

## 2. Definition

Data Access Request Fulfilment Time (DARFT) measures how efficiently resources are converted into outputs in the Data Governance & Stewardship domain. It is a working-level control: thresholds trigger immediate operational response. It is defined as Days to Fulfil Approved Data Access Request; the result is stated in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
DARFT = Days to Fulfil Approved Data Access Request
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** data_governance_stewardship

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3609 (batch 8)
