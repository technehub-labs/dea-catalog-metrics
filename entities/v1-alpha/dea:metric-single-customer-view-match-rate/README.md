# dea:metric-single-customer-view-match-rate

Candidate Performance Metric record for **Single Customer View Match Rate** (SCVM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-single-customer-view-match-rate`
- **Name:** Single Customer View Match Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SCVM

## 2. Definition

Within Customer Analytics & Insights, Single Customer View Match Rate (SCVM) is used to gauge the quality of outputs and outcomes. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Profiles Matched across Sources / Profiles Processed; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of customer records accurately unified across systems. It matters because identity resolution failures break personalization and attribution. Match thresholds can be loosened to claim high unification, creating duplicate-blended profiles. Read with Data Accuracy Rate and duplicate record audits to confirm the view is trustworthy.

## Formula

```
Profiles Matched across Sources / Profiles Processed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** customer_analytics_insights

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1426 (batch 5)
