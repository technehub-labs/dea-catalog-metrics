# dea:metric-crash-free-session-rate

Candidate Performance Metric record for **Crash-Free Session Rate** (CFSR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-crash-free-session-rate`
- **Name:** Crash-Free Session Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CFSR

## 2. Definition

Within Gaming, Crash-Free Session Rate (CFSR) is used to gauge the quality of outputs and outcomes. It is defined as Sessions without Crash / Total Sessions; the result is stated in percent (%). In Gaming, it is a recognized element of the standard performance toolkit. It is a working-level control: thresholds trigger immediate operational response. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
CFSR = Sessions without Crash / Total Sessions
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 713 (batch 2)
