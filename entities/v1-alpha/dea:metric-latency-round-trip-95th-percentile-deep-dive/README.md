# dea:metric-latency-round-trip-95th-percentile-deep-dive

Candidate Performance Metric record for **Latency - Round Trip 95th Percentile (Deep Dive)** (RTT95) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-latency-round-trip-95th-percentile-deep-dive`
- **Name:** Latency - Round Trip 95th Percentile (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RTT95

## 2. Definition

Within Telecom Network Operations (Deep Dive), Latency - Round Trip 95th Percentile (Deep Dive) (RTT95) is used to gauge the quality of outputs and outcomes. It is computed as 95th Percentile Round-Trip Time, expressed in milliseconds (ms). Its use is concentrated in Telecommunications. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
95th Percentile Round-Trip Time
```

## Unit

- **Unit reference:** `dea:unit-millisecond`
- **Unit:** millisecond
- **Unit label (as published):** milliseconds (ms)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** telecom_network_operations_deep_dive
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2129 (batch 6)
