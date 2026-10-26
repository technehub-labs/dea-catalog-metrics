# dea:metric-wan-link-utilization-peak

Candidate Performance Metric record for **WAN Link Utilization Peak** (WLUP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-wan-link-utilization-peak`
- **Name:** WAN Link Utilization Peak
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** WLUP

## 2. Definition

A Network Performance & Capacity indicator, WAN Link Utilization Peak (WLUP) quantifies the utilization or availability of capacity. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Peak Period Traffic / Circuit Capacity - reported in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Peak Period Traffic / Circuit Capacity
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3341 (batch 7)
