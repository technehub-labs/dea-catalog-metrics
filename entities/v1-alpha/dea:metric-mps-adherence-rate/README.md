# dea:metric-mps-adherence-rate

Candidate Performance Metric record for **MPS Adherence Rate** (MPSA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mps-adherence-rate`
- **Name:** MPS Adherence Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MPSA

## 2. Definition

MPS Adherence Rate (MPSA) measures conformance to standards, plans, or obligations in the Supply Chain Standard Measures (Deep Dive) domain. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Production Realized per Master Schedule / Scheduled - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Production Realized per Master Schedule / Scheduled
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** supply_chain_standard_measures_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4266 (batch 10)
