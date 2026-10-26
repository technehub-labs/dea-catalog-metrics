# dea:metric-failover-recovery-time-network

Candidate Performance Metric record for **Failover Recovery Time (Network)** (FRTN) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-failover-recovery-time-network`
- **Name:** Failover Recovery Time (Network)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FRTN

## 2. Definition

Within Network Performance & Capacity, Failover Recovery Time (Network) (FRTN) is used to gauge exposure to adverse outcomes. It provides the day-to-day signal that a process is running as designed. Its calculation is Time to Restore Traffic over Redundant Path, measured in seconds. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Time to Restore Traffic over Redundant Path
```

## Unit

- **Unit reference:** `dea:unit-second`
- **Unit:** second
- **Unit label (as published):** seconds

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** network_performance_capacity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3352 (batch 7)
