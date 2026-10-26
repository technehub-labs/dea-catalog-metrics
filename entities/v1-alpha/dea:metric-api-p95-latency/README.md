# dea:metric-api-p95-latency

Candidate Performance Metric record for **API P95 Latency** (APIP95) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-api-p95-latency`
- **Name:** API P95 Latency
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** APIP95

## 2. Definition

A API Lifecycle Management indicator, API P95 Latency (APIP95) quantifies the quality of outputs and outcomes. It is defined as 95th Percentile Round-Trip Response Time; the result is stated in milliseconds (ms). It is a working-level control: thresholds trigger immediate operational response. Lower values are better; each reduction is an improvement. In Software, it is a recognized element of the standard performance toolkit.

## Formula

```
95th Percentile Round-Trip Response Time
```

## Unit

- **Unit reference:** `dea:unit-milliseconds`
- **Unit:** milliseconds
- **Unit label (as published):** milliseconds (ms)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3214 (batch 7)
