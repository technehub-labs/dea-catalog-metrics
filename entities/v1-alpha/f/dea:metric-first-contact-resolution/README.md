# dea:metric-first-contact-resolution

Candidate Performance Metric record for **First Contact Resolution** (FCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-first-contact-resolution`
- **Name:** First Contact Resolution
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FCR

## 2. Definition

First Contact Resolution (FCR) addresses the quality of outputs and outcomes and is a fixture of customer reporting. It is defined as Issues Resolved on First Contact / Total Issues; the result is stated in percent (%). It is a working-level control: thresholds trigger immediate operational response. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
FCR = Issues Resolved on First Contact / Total Issues
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** customer

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 74 (batch 1)
