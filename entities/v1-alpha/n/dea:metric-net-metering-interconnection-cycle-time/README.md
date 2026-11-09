# dea:metric-net-metering-interconnection-cycle-time

Candidate Performance Metric record for **Net Metering Interconnection Cycle Time** (NMICT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-net-metering-interconnection-cycle-time`
- **Name:** Net Metering Interconnection Cycle Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** NMICT

## 2. Definition

A Utilities Field Operations & Grid indicator, Net Metering Interconnection Cycle Time (NMICT) quantifies how efficiently resources are converted into outputs. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Days from Application to Permission to Operate, measured in days. It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Utilities practice.

## Formula

```
NMICT = Days from Application to Permission to Operate
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** utilities_field_operations_grid
- **Sector:** utilities

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1894 (batch 6)
