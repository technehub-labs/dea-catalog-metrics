# dea:metric-standard-cost-update-frequency

Candidate Performance Metric record for **Standard Cost Update Frequency** (SCUF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-standard-cost-update-frequency`
- **Name:** Standard Cost Update Frequency
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SCUF

## 2. Definition

Standard Cost Update Frequency (SCUF) measures conformance to standards, plans, or obligations in the Product Costing & Margin Management domain. Its calculation is Days since Last Standard Cost Roll, measured in days. It is applied across virtually every sector. It provides the day-to-day signal that a process is running as designed. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Days since Last Standard Cost Roll
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** financial
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** product_costing_margin_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1244 (batch 4)
