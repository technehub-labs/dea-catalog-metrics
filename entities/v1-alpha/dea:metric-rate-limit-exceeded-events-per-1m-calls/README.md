# dea:metric-rate-limit-exceeded-events-per-1m-calls

Candidate Performance Metric record for **Rate-Limit Exceeded Events per 1M Calls** (RLE1M) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-rate-limit-exceeded-events-per-1m-calls`
- **Name:** Rate-Limit Exceeded Events per 1M Calls
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RLE1M

## 2. Definition

Within Software Product Operations (Deep Dive), Rate-Limit Exceeded Events per 1M Calls (RLE1M) is used to gauge the quality of outputs and outcomes. It is defined as 429 Responses / API Calls x 1,000,000; the result is stated in events per thousand or million (scaled). In Technology, it is a recognized element of the standard performance toolkit. It is a working-level control: thresholds trigger immediate operational response. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
RLE1M = 429 Responses / API Calls x 1,000,000
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** software_product_operations_deep_dive
- **Sector:** technology

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2163 (batch 6)
