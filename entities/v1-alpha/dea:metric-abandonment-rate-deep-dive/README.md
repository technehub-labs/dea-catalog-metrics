# dea:metric-abandonment-rate-deep-dive

Candidate Performance Metric record for **Abandonment Rate (Deep Dive)** (ABR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-abandonment-rate-deep-dive`
- **Name:** Abandonment Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ABR-D

## 2. Definition

Within Contact Center Operations (Deep Dive), Abandonment Rate (Deep Dive) (ABR-D) is used to gauge the quality of outputs and outcomes. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Calls Abandoned / Calls Offered, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
ABR-D = Calls Abandoned / Calls Offered
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
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contact_center_operations_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2483 (batch 6)
