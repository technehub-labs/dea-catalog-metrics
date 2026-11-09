# dea:metric-freight-wagon-turnaround-time

Candidate Performance Metric record for **Freight Wagon Turnaround Time** (FWTT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-freight-wagon-turnaround-time`
- **Name:** Freight Wagon Turnaround Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FWTT

## 2. Definition

Freight Wagon Turnaround Time (FWTT) addresses how efficiently resources are converted into outputs and is a fixture of rail transport reporting. It is computed as Days from Loading to Return for Loading, expressed in days. Its use is concentrated in Rail. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
FWTT = Days from Loading to Return for Loading
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** rail_transport
- **Sector:** rail

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 998 (batch 3)
