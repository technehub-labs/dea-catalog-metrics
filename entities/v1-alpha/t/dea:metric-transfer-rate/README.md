# dea:metric-transfer-rate

Candidate Performance Metric record for **Transfer Rate** (TRF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-transfer-rate`
- **Name:** Transfer Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TRF

## 2. Definition

Transfer Rate (TRF) captures the quality of outputs and outcomes for organizations tracking contact center. Its calculation is Transferred Calls / Total Calls, measured in percent (%). It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
TRF = Transferred Calls / Total Calls
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contact_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 569 (batch 2)
