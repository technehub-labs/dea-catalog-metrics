# dea:metric-network-availability-sites

Candidate Performance Metric record for **Network Availability (Sites)** (NAS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-network-availability-sites`
- **Name:** Network Availability (Sites)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** NAS

## 2. Definition

A Network Performance & Capacity indicator, Network Availability (Sites) (NAS) quantifies the quality of outputs and outcomes. It is computed as Site Uptime Minutes / Planned Uptime Minutes, expressed in percent (%). It is applied across virtually every sector. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
NAS = Site Uptime Minutes / Planned Uptime Minutes
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** network_performance_capacity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3340 (batch 7)
