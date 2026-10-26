# dea:metric-fault-repeat-rate

Candidate Performance Metric record for **Fault Repeat Rate** (FRR-N) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fault-repeat-rate`
- **Name:** Fault Repeat Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FRR-N

## 2. Definition

Fault Repeat Rate (FRR-N) measures the quality of outputs and outcomes in the Telecom Network Operations domain. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Faults Reoccurring within 30 Days / Faults Repaired - reported in percent (%). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Telecommunications sector.

## Formula

```
Faults Reoccurring within 30 Days / Faults Repaired
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** telecom_network_operations
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 868 (batch 3)
