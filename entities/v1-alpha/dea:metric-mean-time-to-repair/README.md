# dea:metric-mean-time-to-repair

Candidate Performance Metric record for **Mean Time to Repair** (MTTR-M) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mean-time-to-repair`
- **Name:** Mean Time to Repair
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MTTR-M

## 2. Definition

A Maintenance & Reliability indicator, Mean Time to Repair (MTTR-M) quantifies how efficiently resources are converted into outputs. It is computed as Total Repair Time / Number of Repairs, expressed in hours. Its use is concentrated in Manufacturing. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Total Repair Time / Number of Repairs
```

## Unit

- **Unit reference:** `dea:unit-hours`
- **Unit:** hours
- **Unit label (as published):** hours

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** maintenance_reliability
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 267 (batch 1)
