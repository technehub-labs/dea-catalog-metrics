# dea:metric-identity-access-review-timeliness

Candidate Performance Metric record for **Identity Access Review Timeliness** (IART) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-identity-access-review-timeliness`
- **Name:** Identity Access Review Timeliness
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** IART

## 2. Definition

Identity Access Review Timeliness (IART) addresses conformance to standards, plans, or obligations and is a fixture of cybersecurity reporting. The formula is Access Reviews Completed On Time / Reviews Due - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
IART = Access Reviews Completed On Time / Reviews Due
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** cybersecurity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 329 (batch 1)
