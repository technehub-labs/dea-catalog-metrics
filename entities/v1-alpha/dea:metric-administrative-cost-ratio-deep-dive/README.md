# dea:metric-administrative-cost-ratio-deep-dive

Candidate Performance Metric record for **Administrative Cost Ratio (Deep Dive)** (ACR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-administrative-cost-ratio-deep-dive`
- **Name:** Administrative Cost Ratio (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ACR-D

## 2. Definition

A Nonprofit & Donor Operations (Deep Dive) indicator, Administrative Cost Ratio (Deep Dive) (ACR-D) quantifies how efficiently resources are converted into outputs. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Administrative Expenses / Total Expenses - reported in percent (%). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Nonprofit sector.

## 3. Context

Measures the share of spending on administration and overhead. It is the capacity-investment honesty metric: chronic under-investment shows up as staff turnover, compliance failures, and program fragility, while unmanaged growth shows up as an overhead creep the mission does not feel. The ratio should be read against functional benchmarks, not a naive lower-is-better instinct. Read with program spend ratio (Deep Dive) and staff capacity indicators.

## Formula

```
ACR-D = Administrative Expenses / Total Expenses
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** nonprofit_donor_operations_deep_dive
- **Sector:** nonprofit

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2461 (batch 6)
