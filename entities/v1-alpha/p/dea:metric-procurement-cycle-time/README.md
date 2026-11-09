# dea:metric-procurement-cycle-time

Candidate Performance Metric record for **Procurement Cycle Time** (PCT-P) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-procurement-cycle-time`
- **Name:** Procurement Cycle Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PCT-P

## 2. Definition

Procurement Cycle Time (PCT-P) measures how efficiently resources are converted into outputs in the Procurement domain. The formula is Days from Requisition to Purchase Order Issue - reported in days. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
PCT-P = Days from Requisition to Purchase Order Issue
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** procurement

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 222 (batch 1)
