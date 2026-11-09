# dea:metric-crowd-density-compliance-rate

Candidate Performance Metric record for **Crowd Density Compliance Rate** (CDCR-E) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-crowd-density-compliance-rate`
- **Name:** Crowd Density Compliance Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CDCR-E

## 2. Definition

Crowd Density Compliance Rate (CDCR-E) measures exposure to adverse outcomes in the Events & Exhibitions domain. It is computed as Times within Density Limits / Monitoring Periods, expressed in percent (%). Its use is concentrated in Media & Entertainment. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
CDCR-E = Times within Density Limits / Monitoring Periods
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** events_exhibitions
- **Sector:** media_entertainment

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1943 (batch 6)
