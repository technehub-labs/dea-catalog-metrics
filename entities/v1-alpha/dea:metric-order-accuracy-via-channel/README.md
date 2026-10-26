# dea:metric-order-accuracy-via-channel

Candidate Performance Metric record for **Order Accuracy via Channel** (OAVC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-order-accuracy-via-channel`
- **Name:** Order Accuracy via Channel
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** OAVC

## 2. Definition

A Channel & Distribution Management indicator, Order Accuracy via Channel (OAVC) quantifies the quality of outputs and outcomes. It is defined as Channel Orders Filled without Correction / Channel Orders; the result is stated in percent (%). It is a working-level control: thresholds trigger immediate operational response. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Channel Orders Filled without Correction / Channel Orders
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** channel_distribution_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3989 (batch 8)
