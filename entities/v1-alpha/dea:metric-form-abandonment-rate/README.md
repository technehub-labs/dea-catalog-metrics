# dea:metric-form-abandonment-rate

Candidate Performance Metric record for **Form Abandonment Rate** (FAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-form-abandonment-rate`
- **Name:** Form Abandonment Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FAR

## 2. Definition

Form Abandonment Rate (FAR) measures exposure to adverse outcomes in the Digital Product & Web Operations domain. It provides the day-to-day signal that a process is running as designed. Its calculation is Forms Started but Not Submitted / Forms Started, measured in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Forms Started but Not Submitted / Forms Started
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** digital_product_web_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1082 (batch 4)
