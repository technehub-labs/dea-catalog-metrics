# dea:metric-workload-placement-efficiency

Candidate Performance Metric record for **Workload Placement Efficiency** (WPE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-workload-placement-efficiency`
- **Name:** Workload Placement Efficiency
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** WPE

## 2. Definition

Workload Placement Efficiency (WPE) addresses how efficiently resources are converted into outputs and is a fixture of data centers & cloud infrastructure reporting. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Workloads on Optimal Tier / Workloads, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Technology practice.

## 3. Context

Measures how well workloads are placed across the fleet - matching workload requirements to optimal sites for cost, latency, and resilience. It is the margin metric of cloud and colocation economics: misplaced workloads burn premium power and cooling in sites designed for other purposes. Placement optimized for cost that violates latency or availability requirements is false efficiency. Read with utilization by resource type and cooling-efficiency trends.

## Formula

```
WPE = Workloads on Optimal Tier / Workloads
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** data_centers_cloud_infrastructure
- **Sector:** technology

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2144 (batch 6)
