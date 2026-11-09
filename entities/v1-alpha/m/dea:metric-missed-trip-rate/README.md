# dea:metric-missed-trip-rate

Candidate Performance Metric record for **Missed Trip Rate** (MTR-P) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-missed-trip-rate`
- **Name:** Missed Trip Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MTR-P

## 2. Definition

Missed Trip Rate (MTR-P) addresses the quality of outputs and outcomes and is a fixture of public transit reporting. It is computed as Trips Not Operated / Trips Scheduled, expressed in percent (%). Its use is concentrated in Public transit. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
MTR-P = Trips Not Operated / Trips Scheduled
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** public_transit
- **Sector:** public_transit

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1003 (batch 3)
