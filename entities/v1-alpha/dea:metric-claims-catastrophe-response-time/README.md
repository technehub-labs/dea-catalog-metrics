# dea:metric-claims-catastrophe-response-time

Candidate Performance Metric record for **Claims Catastrophe Response Time** (CCRT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-claims-catastrophe-response-time`
- **Name:** Claims Catastrophe Response Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CCRT

## 2. Definition

Claims Catastrophe Response Time (CCRT) measures how efficiently resources are converted into outputs in the Insurance Claims Deep Dive domain. The formula is Hours from Catastrophe Event to First Claim Response - reported in hours. It is a standard measure in the Insurance sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
CCRT = Hours from Catastrophe Event to First Claim Response
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_claims_deep_dive
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1554 (batch 6)
