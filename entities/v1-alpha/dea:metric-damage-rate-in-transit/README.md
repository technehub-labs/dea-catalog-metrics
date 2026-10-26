# dea:metric-damage-rate-in-transit

Candidate Performance Metric record for **Damage Rate in Transit** (DRIT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-damage-rate-in-transit`
- **Name:** Damage Rate in Transit
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DRIT

## 2. Definition

A Supply Chain indicator, Damage Rate in Transit (DRIT) quantifies the quality of outputs and outcomes. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Damaged Units on Arrival / Units Shipped - reported in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Damaged Units on Arrival / Units Shipped
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** supply_chain

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 191 (batch 1)
