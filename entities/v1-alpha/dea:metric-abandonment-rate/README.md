# dea:metric-abandonment-rate

Candidate Performance Metric record for **Abandonment Rate** (ABR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-abandonment-rate`
- **Name:** Abandonment Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ABR

## 2. Definition

A Contact Center indicator, Abandonment Rate (ABR) quantifies the quality of outputs and outcomes. Its calculation is Abandoned Calls / Calls Offered, measured in percent (%). It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Abandoned Calls / Calls Offered
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 564 (batch 2)
