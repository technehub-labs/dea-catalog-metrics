# dea:metric-duplicate-survivor-rate-mdm

Candidate Performance Metric record for **Duplicate Survivor Rate (MDM)** (DSR-MD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-duplicate-survivor-rate-mdm`
- **Name:** Duplicate Survivor Rate (MDM)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DSR-MD

## 2. Definition

Duplicate Survivor Rate (MDM) (DSR-MD) measures the quality of outputs and outcomes in the Master Data Management domain. It is a working-level control: thresholds trigger immediate operational response. It is defined as Remaining Duplicate Masters after Matching / Masters; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Remaining Duplicate Masters after Matching / Masters
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** master_data_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3639 (batch 8)
