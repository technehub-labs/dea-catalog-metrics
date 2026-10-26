# dea:metric-reserved-instance-coverage

Candidate Performance Metric record for **Reserved Instance Coverage** (RIC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-reserved-instance-coverage`
- **Name:** Reserved Instance Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RIC

## 2. Definition

Within Data Center & Cloud Operations, Reserved Instance Coverage (RIC) is used to gauge how efficiently resources are converted into outputs. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Workloads on Reserved Capacity / Total Workloads - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Technology & data centers sector.

## 3. Context

Measures the share of cloud compute spend covered by committed-use discounts. It matters because commitment coverage is the largest single cloud cost lever. Over-committing to hit coverage targets locks in waste if workloads shift. Read with Instance Right-Sizing findings and cloud spend variance to confirm coverage is efficient.

## Formula

```
Workloads on Reserved Capacity / Total Workloads
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** data_center_cloud_operations
- **Sector:** technology_data_centers

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1093 (batch 4)
