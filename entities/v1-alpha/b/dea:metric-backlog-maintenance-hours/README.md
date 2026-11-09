# dea:metric-backlog-maintenance-hours

Candidate Performance Metric record for **Backlog Maintenance Hours** (BMH) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-backlog-maintenance-hours`
- **Name:** Backlog Maintenance Hours
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BMH

## 2. Definition

Backlog Maintenance Hours (BMH) addresses the utilization or availability of capacity and is a fixture of maintenance & reliability reporting. The formula is Outstanding Maintenance Work Hours - reported in hours. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Lower values are better; each reduction is an improvement. It is a standard measure in the Manufacturing sector.

## Formula

```
BMH = Outstanding Maintenance Work Hours
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 271 (batch 1)
