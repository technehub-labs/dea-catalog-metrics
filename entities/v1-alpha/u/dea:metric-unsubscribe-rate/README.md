# dea:metric-unsubscribe-rate

Candidate Performance Metric record for **Unsubscribe Rate** (USR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-unsubscribe-rate`
- **Name:** Unsubscribe Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** USR

## 2. Definition

Within Marketing, Unsubscribe Rate (USR) is used to gauge exposure to adverse outcomes. The formula is Unsubscribes / Emails Delivered - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
USR = Unsubscribes / Emails Delivered
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** marketing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 117 (batch 1)
