# dea:metric-security-screening-throughput-rate

Candidate Performance Metric record for **Security Screening Throughput Rate** (SSTR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-security-screening-throughput-rate`
- **Name:** Security Screening Throughput Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SSTR

## 2. Definition

Within Airport Operations (Deep Dive), Security Screening Throughput Rate (SSTR) is used to gauge the utilization or availability of capacity. It is defined as Passengers Screened per Lane Hour; the result is stated in count (items per period). In Aviation, it is a recognized element of the standard performance toolkit. It is a working-level control: thresholds trigger immediate operational response. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Passengers Screened per Lane Hour
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airport_operations_deep_dive
- **Sector:** aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2271 (batch 6)
