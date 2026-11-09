# dea:metric-complaint-rate

Candidate Performance Metric record for **Complaint Rate** (CoR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-complaint-rate`
- **Name:** Complaint Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CoR

## 2. Definition

A Customer indicator, Complaint Rate (CoR) quantifies the quality of outputs and outcomes. Its calculation is Complaints / Total Customer Interactions, measured in ratio (x:1 or x). It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
CoR = Complaints / Total Customer Interactions
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** customer

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 76 (batch 1)
