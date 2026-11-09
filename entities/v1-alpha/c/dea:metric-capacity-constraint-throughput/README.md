# dea:metric-capacity-constraint-throughput

Candidate Performance Metric record for **Capacity Constraint Throughput** (CCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-capacity-constraint-throughput`
- **Name:** Capacity Constraint Throughput
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CCT

## 2. Definition

Capacity Constraint Throughput (CCT) measures the utilization or availability of capacity in the Manufacturing domain. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Units through Constraint per Shift - reported in count (items per period). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Manufacturing sector.

## Formula

```
CCT = Units through Constraint per Shift
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
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** manufacturing
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 253 (batch 1)
