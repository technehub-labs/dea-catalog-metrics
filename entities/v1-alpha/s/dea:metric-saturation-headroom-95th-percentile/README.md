# dea:metric-saturation-headroom-95th-percentile

Candidate Performance Metric record for **Saturation Headroom - 95th Percentile** (SH95) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-saturation-headroom-95th-percentile`
- **Name:** Saturation Headroom - 95th Percentile
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SH95

## 2. Definition

Saturation Headroom - 95th Percentile (SH95) captures the utilization or availability of capacity for organizations tracking observability & site reliability engineering. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is 95th Percentile Resource Utilization - reported in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## Formula

```
SH95 = 95th Percentile Resource Utilization
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** observability_site_reliability_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2873 (batch 7)
