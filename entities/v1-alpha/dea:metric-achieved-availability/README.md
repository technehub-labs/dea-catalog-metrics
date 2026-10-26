# dea:metric-achieved-availability

Candidate Performance Metric record for **Achieved Availability** (ACAVL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-achieved-availability`
- **Name:** Achieved Availability
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ACAVL

## 2. Definition

Achieved Availability (ACAVL) addresses the quality of outputs and outcomes and is a fixture of reliability & maintainability engineering (deep dive) reporting. It is defined as MTBMA / (MTBMA + MMTRS); the result is stated in percent (%). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
MTBMA / (MTBMA + MMTRS)
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** capability
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** reliability_maintainability_engineering_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4102 (batch 9)
