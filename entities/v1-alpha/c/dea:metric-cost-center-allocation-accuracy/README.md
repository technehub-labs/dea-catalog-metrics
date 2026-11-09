# dea:metric-cost-center-allocation-accuracy

Candidate Performance Metric record for **Cost Center Allocation Accuracy** (CCAA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-center-allocation-accuracy`
- **Name:** Cost Center Allocation Accuracy
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CCAA

## 2. Definition

Cost Center Allocation Accuracy (CCAA) addresses conformance to standards, plans, or obligations and is a fixture of financial planning & analysis reporting. Its calculation is Allocations per Documented Policy / Allocation Lines, measured in percent (%). It provides the day-to-day signal that a process is running as designed. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
CCAA = Allocations per Documented Policy / Allocation Lines
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** financial_planning_analysis

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3788 (batch 8)
