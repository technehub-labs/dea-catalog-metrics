# dea:metric-maintenance-request-resolution-time

Candidate Performance Metric record for **Maintenance Request Resolution Time** (MRRT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-maintenance-request-resolution-time`
- **Name:** Maintenance Request Resolution Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MRRT

## 2. Definition

Within Facilities & Real Estate, Maintenance Request Resolution Time (MRRT) is used to gauge how efficiently resources are converted into outputs. The formula is Hours from Request to Completion - reported in hours. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
MRRT = Hours from Request to Completion
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** facilities_real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 452 (batch 1)
