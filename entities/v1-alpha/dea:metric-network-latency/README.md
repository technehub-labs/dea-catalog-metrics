# dea:metric-network-latency

Candidate Performance Metric record for **Network Latency** (NL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-network-latency`
- **Name:** Network Latency
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** NL

## 2. Definition

A Telecommunications indicator, Network Latency (NL) quantifies the quality of outputs and outcomes. It is a working-level control: thresholds trigger immediate operational response. It is defined as Median Round-Trip Delay of Packets; the result is stated in seconds. It should be driven down, since lower readings signal healthier performance. In Telecommunications, it is a recognized element of the standard performance toolkit.

## Formula

```
Median Round-Trip Delay of Packets
```

## Unit

- **Unit reference:** `dea:unit-seconds`
- **Unit:** seconds
- **Unit label (as published):** seconds

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** telecommunications
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 532 (batch 1)
