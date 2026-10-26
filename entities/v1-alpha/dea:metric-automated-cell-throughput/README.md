# dea:metric-automated-cell-throughput

Candidate Performance Metric record for **Automated Cell Throughput** (ACT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-automated-cell-throughput`
- **Name:** Automated Cell Throughput
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ACT

## 2. Definition

A Industrial Automation & Robotics indicator, Automated Cell Throughput (ACT) quantifies the utilization or availability of capacity. It is defined as Units Produced per Automated Cell per Shift; the result is stated in count (items per period). It is a working-level control: thresholds trigger immediate operational response. Higher values are better; gains are read as improvement and losses as deterioration. In Manufacturing, it is a recognized element of the standard performance toolkit.

## Formula

```
Units Produced per Automated Cell per Shift
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** industrial_automation_robotics
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1337 (batch 5)
