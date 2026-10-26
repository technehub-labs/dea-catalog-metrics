# dea:metric-api-breaking-change-rate-deep-dive

Candidate Performance Metric record for **API Breaking Change Rate (Deep Dive)** (APIBC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-api-breaking-change-rate-deep-dive`
- **Name:** API Breaking Change Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** APIBC

## 2. Definition

A API Lifecycle Management indicator, API Breaking Change Rate (Deep Dive) (APIBC) quantifies exposure to adverse outcomes. It is computed as Breaking Changes Released / Releases with API Changes, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Lower values are better; each reduction is an improvement. Its use is concentrated in Software.

## Formula

```
Breaking Changes Released / Releases with API Changes
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** api_lifecycle_management
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3208 (batch 7)
