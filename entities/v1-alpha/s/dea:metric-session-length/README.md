# dea:metric-session-length

Candidate Performance Metric record for **Session Length** (SGL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-session-length`
- **Name:** Session Length
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SGL

## 2. Definition

Session Length (SGL) addresses the engagement or satisfaction of the people involved and is a fixture of gaming reporting. It is defined as Total Play Time / Sessions; the result is stated in minutes. In Gaming, it is a recognized element of the standard performance toolkit. It is a working-level control: thresholds trigger immediate operational response. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
SGL = Total Play Time / Sessions
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** engagement
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** gaming
- **Sector:** gaming

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 706 (batch 2)
