# dea:metric-broken-build-recovery-time

Candidate Performance Metric record for **Broken Build Recovery Time** (BBRT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-broken-build-recovery-time`
- **Name:** Broken Build Recovery Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BBRT

## 2. Definition

Within Continuous Integration, Broken Build Recovery Time (BBRT) is used to gauge how efficiently resources are converted into outputs. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Minutes to Restore Green Build after Failure - reported in minutes. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Minutes to Restore Green Build after Failure
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** continuous_integration

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2666 (batch 7)
