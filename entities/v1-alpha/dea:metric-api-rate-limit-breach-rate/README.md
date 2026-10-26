# dea:metric-api-rate-limit-breach-rate

Candidate Performance Metric record for **API Rate Limit Breach Rate** (APRLB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-api-rate-limit-breach-rate`
- **Name:** API Rate Limit Breach Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** APRLB

## 2. Definition

API Rate Limit Breach Rate (APRLB) addresses the utilization or availability of capacity and is a fixture of api lifecycle management reporting. It is defined as Throttled Requests / Total Requests; the result is stated in percent (%). In Software, it is a recognized element of the standard performance toolkit. It is a working-level control: thresholds trigger immediate operational response. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Throttled Requests / Total Requests
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3215 (batch 7)
