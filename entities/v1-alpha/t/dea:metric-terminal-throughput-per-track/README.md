# dea:metric-terminal-throughput-per-track

Candidate Performance Metric record for **Terminal Throughput per Track** (TTPT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-terminal-throughput-per-track`
- **Name:** Terminal Throughput per Track
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TTPT

## 2. Definition

Terminal Throughput per Track (TTPT) captures the utilization or availability of capacity for organizations tracking rail freight (deep dive). It is computed as Cars Handled / Track Day, expressed in count (items per period). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Rail.

## Formula

```
TTPT = Cars Handled / Track Day
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** rail_freight_deep_dive
- **Sector:** rail

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2427 (batch 6)
