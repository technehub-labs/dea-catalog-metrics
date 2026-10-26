# dea:metric-cell-outage-rate

Candidate Performance Metric record for **Cell Outage Rate** (COR-N) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cell-outage-rate`
- **Name:** Cell Outage Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** COR-N

## 2. Definition

A Telecom Network Operations indicator, Cell Outage Rate (COR-N) quantifies exposure to adverse outcomes. It provides the day-to-day signal that a process is running as designed. Its calculation is Cell Sites Out of Service / Total Cell Sites, measured in percent (%). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Telecommunications practice.

## Formula

```
COR-N = Cell Sites Out of Service / Total Cell Sites
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** telecom_network_operations
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 860 (batch 3)
