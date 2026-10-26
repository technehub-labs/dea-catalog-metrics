# dea:metric-address-quality-correction-rate

Candidate Performance Metric record for **Address Quality Correction Rate** (AQC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-address-quality-correction-rate`
- **Name:** Address Quality Correction Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** AQC

## 2. Definition

Address Quality Correction Rate (AQC) measures the quality of outputs and outcomes in the Postal & Courier domain. It provides the day-to-day signal that a process is running as designed. Its calculation is Items Requiring Address Correction / Items Received, measured in percent (%). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Postal & courier practice.

## Formula

```
Items Requiring Address Correction / Items Received
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
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
- **Domain:** postal_courier
- **Sector:** postal_courier

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 832 (batch 2)
