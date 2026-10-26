# dea:metric-passenger-information-accuracy

Candidate Performance Metric record for **Passenger Information Accuracy** (PIA-T) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-passenger-information-accuracy`
- **Name:** Passenger Information Accuracy
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PIA-T

## 2. Definition

Passenger Information Accuracy (PIA-T) measures the quality of outputs and outcomes in the Public Transit (Deep Dive) domain. The formula is Real-Time Predictions within Tolerance / Predictions - reported in percent (%). It is a standard measure in the Public Transit sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Real-Time Predictions within Tolerance / Predictions
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** public_transit_deep_dive
- **Sector:** public_transit

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2414 (batch 6)
