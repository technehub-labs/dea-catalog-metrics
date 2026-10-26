# dea:metric-capacity-to-demand-match-index

Candidate Performance Metric record for **Capacity-to-Demand Match Index** (CDMI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-capacity-to-demand-match-index`
- **Name:** Capacity-to-Demand Match Index
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CDMI

## 2. Definition

A Workforce Planning & Productivity indicator, Capacity-to-Demand Match Index (CDMI) quantifies the utilization or availability of capacity. Its calculation is Available Capacity vs Demand across Skills, measured in index (0-100 or normalized). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how well available workforce capacity aligns with demand patterns across time. Mismatch shows up as both overtime burn and idle capacity simultaneously. Match measured at monthly level misses intra-month peaks. Read with capacity forecast accuracy and labor cost percentage.

## Formula

```
Available Capacity vs Demand across Skills
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** organization
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** workforce_planning_productivity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3901 (batch 8)
