# dea:metric-spares-provisioning-adequacy

Candidate Performance Metric record for **Spares Provisioning Adequacy** (SPA-RM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-spares-provisioning-adequacy`
- **Name:** Spares Provisioning Adequacy
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SPA-RM

## 2. Definition

Spares Provisioning Adequacy (SPA-RM) addresses the utilization or availability of capacity and is a fixture of reliability & maintainability engineering (deep dive) reporting. It is defined as Demand Met from Stock / Total Spares Demand; the result is stated in percent (%). It is a working-level control: thresholds trigger immediate operational response. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
SPA-RM = Demand Met from Stock / Total Spares Demand
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** capability
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** reliability_maintainability_engineering_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4110 (batch 9)
