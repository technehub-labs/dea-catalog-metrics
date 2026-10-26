# dea:metric-wireless-client-density-capacity-index

Candidate Performance Metric record for **Wireless Client Density Capacity Index** (WCDI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-wireless-client-density-capacity-index`
- **Name:** Wireless Client Density Capacity Index
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** WCDI

## 2. Definition

Wireless Client Density Capacity Index (WCDI) measures the utilization or availability of capacity in the Network Performance & Capacity domain. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Concurrent Clients per AP vs Design Threshold - reported in index (0-100 or normalized). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Concurrent Clients per AP vs Design Threshold
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** network_performance_capacity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3354 (batch 7)
