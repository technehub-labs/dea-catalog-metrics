# dea:metric-interface-error-rate

Candidate Performance Metric record for **Interface Error Rate** (IER-NW) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-interface-error-rate`
- **Name:** Interface Error Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** IER-NW

## 2. Definition

Interface Error Rate (IER-NW) measures the quality of outputs and outcomes in the Network Performance & Capacity domain. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Interfaces with Persistent Errors / Interfaces - reported in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Interfaces with Persistent Errors / Interfaces
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** network_performance_capacity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3353 (batch 7)
