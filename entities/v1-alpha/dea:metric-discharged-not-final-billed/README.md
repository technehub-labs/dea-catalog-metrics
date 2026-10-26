# dea:metric-discharged-not-final-billed

Candidate Performance Metric record for **Discharged Not Final Billed** (DNFB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-discharged-not-final-billed`
- **Name:** Discharged Not Final Billed
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DNFB

## 2. Definition

Within Healthcare Revenue Cycle, Discharged Not Final Billed (DNFB) is used to gauge the utilization or availability of capacity. The formula is Discharged Accounts Awaiting Final Billing - reported in count (items per period). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Lower values are better; each reduction is an improvement. It is a standard measure in the Healthcare sector.

## Formula

```
Discharged Accounts Awaiting Final Billing
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** financial
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** healthcare_revenue_cycle
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 877 (batch 3)
