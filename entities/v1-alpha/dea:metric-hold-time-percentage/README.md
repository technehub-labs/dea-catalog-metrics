# dea:metric-hold-time-percentage

Candidate Performance Metric record for **Hold Time Percentage** (HTP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-hold-time-percentage`
- **Name:** Hold Time Percentage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** HTP

## 2. Definition

Hold Time Percentage (HTP) measures the quality of outputs and outcomes in the Contact Center domain. It is defined as Hold Time / Handle Time; the result is stated in percent (%). It is a working-level control: thresholds trigger immediate operational response. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Hold Time / Handle Time
```

## Unit

- **Unit reference:** `dea:unit-percent`
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 571 (batch 2)
