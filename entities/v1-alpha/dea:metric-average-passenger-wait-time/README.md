# dea:metric-average-passenger-wait-time

Candidate Performance Metric record for **Average Passenger Wait Time** (APWT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-passenger-wait-time`
- **Name:** Average Passenger Wait Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** APWT

## 2. Definition

Within Public Transit, Average Passenger Wait Time (APWT) is used to gauge the quality of outputs and outcomes. The formula is Observed Waiting Time at Stops, Averaged - reported in minutes. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Lower values are better; each reduction is an improvement. It is a standard measure in the Public transit sector.

## Formula

```
Observed Waiting Time at Stops, Averaged
```

## Unit

- **Unit reference:** `dea:unit-minutes`
- **Unit:** minutes
- **Unit label (as published):** minutes

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1004 (batch 3)
