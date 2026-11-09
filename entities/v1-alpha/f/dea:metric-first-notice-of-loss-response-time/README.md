# dea:metric-first-notice-of-loss-response-time

Candidate Performance Metric record for **First Notice of Loss Response Time** (FNOLT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-first-notice-of-loss-response-time`
- **Name:** First Notice of Loss Response Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FNOLT

## 2. Definition

A Claims Operations (Insurance) indicator, First Notice of Loss Response Time (FNOLT) quantifies how efficiently resources are converted into outputs. It is defined as Hours from Loss Notification to First Customer Contact; the result is stated in hours. It is a working-level control: thresholds trigger immediate operational response. Lower values are better; each reduction is an improvement. In Insurance, it is a recognized element of the standard performance toolkit.

## Formula

```
FNOLT = Hours from Loss Notification to First Customer Contact
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** claims_operations_insurance
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 849 (batch 3)
