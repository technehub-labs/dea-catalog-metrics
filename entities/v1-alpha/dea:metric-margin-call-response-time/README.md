# dea:metric-margin-call-response-time

Candidate Performance Metric record for **Margin Call Response Time** (MCRT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-margin-call-response-time`
- **Name:** Margin Call Response Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MCRT

## 2. Definition

Margin Call Response Time (MCRT) measures exposure to adverse outcomes in the Investment Risk & Middle Office Operations domain. It is a working-level control: thresholds trigger immediate operational response. It is defined as Time from Call to Funded Response; the result is stated in hours. It should be driven down, since lower readings signal healthier performance. In Investment management, it is a recognized element of the standard performance toolkit.

## Formula

```
Time from Call to Funded Response
```

## Unit

- **Unit reference:** `dea:unit-hours`
- **Unit:** hours
- **Unit label (as published):** hours

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_risk_middle_office_operations
- **Sector:** investment_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3467 (batch 7)
