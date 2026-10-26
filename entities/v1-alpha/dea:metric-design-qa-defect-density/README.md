# dea:metric-design-qa-defect-density

Candidate Performance Metric record for **Design QA Defect Density** (DQDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-design-qa-defect-density`
- **Name:** Design QA Defect Density
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DQDD

## 2. Definition

Design QA Defect Density (DQDD) captures the quality of outputs and outcomes for organizations tracking ux & design systems. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Design QA Issues Found per Screen Delivered - reported in ratio (x:1 or x). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Design QA Issues Found per Screen Delivered
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** ux_design_systems

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3279 (batch 7)
