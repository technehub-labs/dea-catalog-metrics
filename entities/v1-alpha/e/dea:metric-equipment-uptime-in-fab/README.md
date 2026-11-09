# dea:metric-equipment-uptime-in-fab

Candidate Performance Metric record for **Equipment Uptime in Fab** (EUPT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-equipment-uptime-in-fab`
- **Name:** Equipment Uptime in Fab
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** EUPT

## 2. Definition

Equipment Uptime in Fab (EUPT) addresses the utilization or availability of capacity and is a fixture of semiconductor & electronics reporting. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Tool Productive Time / Total Tool Time, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Electronics & semiconductors.

## Formula

```
EUPT = Tool Productive Time / Total Tool Time
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** semiconductor_electronics
- **Sector:** electronics_semiconductors

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 906 (batch 3)
