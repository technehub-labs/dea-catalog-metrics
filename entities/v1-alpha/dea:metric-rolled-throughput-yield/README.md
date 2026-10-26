# dea:metric-rolled-throughput-yield

Candidate Performance Metric record for **Rolled Throughput Yield** (RTYS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-rolled-throughput-yield`
- **Name:** Rolled Throughput Yield
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RTYS

## 2. Definition

Rolled Throughput Yield (RTYS) addresses the quality of outputs and outcomes and is a fixture of process capability & six sigma (deep dive) reporting. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Product of Step Yields across Process Chain - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Manufacturing sector.

## Formula

```
Product of Step Yields across Process Chain
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** capability
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** process_capability_six_sigma_deep_dive
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4082 (batch 9)
