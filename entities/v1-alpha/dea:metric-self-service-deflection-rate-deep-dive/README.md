# dea:metric-self-service-deflection-rate-deep-dive

Candidate Performance Metric record for **Self-Service Deflection Rate (Deep Dive)** (SSDRDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-self-service-deflection-rate-deep-dive`
- **Name:** Self-Service Deflection Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SSDRDD

## 2. Definition

Self-Service Deflection Rate (Deep Dive) (SSDRDD) measures how efficiently resources are converted into outputs in the Contact Center Standard Measures (Deep Dive) domain. It is defined as Contacts Deflected by Self-Service / Total Demand; the result is stated in percent (%). It is applied across virtually every sector. It is a working-level control: thresholds trigger immediate operational response. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Contacts Deflected by Self-Service / Total Demand
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contact_center_standard_measures_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4322 (batch 10)
