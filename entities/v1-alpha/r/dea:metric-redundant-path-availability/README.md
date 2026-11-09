# dea:metric-redundant-path-availability

Candidate Performance Metric record for **Redundant Path Availability** (RPA-NW) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-redundant-path-availability`
- **Name:** Redundant Path Availability
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RPA-NW

## 2. Definition

A Network Performance & Capacity indicator, Redundant Path Availability (RPA-NW) quantifies exposure to adverse outcomes. The formula is Sites with Diverse Redundant Paths / Sites - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures whether failover paths for critical network segments are actually available and healthy. Redundancy that exists in design but not in runtime is a false comfort. Paths not regularly tested fail at exactly the wrong moment. Read with availability zone redundancy compliance and failover test pass rate.

## Formula

```
RPA-NW = Sites with Diverse Redundant Paths / Sites
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** network_performance_capacity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3351 (batch 7)
