# dea:metric-requirements-volatility-index-deep-dive

Candidate Performance Metric record for **Requirements Volatility Index (Deep Dive)** (RVI-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-requirements-volatility-index-deep-dive`
- **Name:** Requirements Volatility Index (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RVI-D

## 2. Definition

Requirements Volatility Index (Deep Dive) (RVI-D) captures exposure to adverse outcomes for organizations tracking project management (deep dive). It is defined as Changed Requirements after Freeze / Baseline Requirements; the result is stated in percent (%). It is applied across virtually every sector. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
RVI-D = Changed Requirements after Freeze / Baseline Requirements
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** project_management_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2937 (batch 7)
