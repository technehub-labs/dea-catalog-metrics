# dea:metric-aircraft-turnaround-compliance

Candidate Performance Metric record for **Aircraft Turnaround Compliance** (ATC-A) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-aircraft-turnaround-compliance`
- **Name:** Aircraft Turnaround Compliance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ATC-A

## 2. Definition

Within Airport Operations, Aircraft Turnaround Compliance (ATC-A) is used to gauge the quality of outputs and outcomes. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Turnarounds within Allocated Time / Turnarounds - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Airports sector.

## Formula

```
ATC-A = Turnarounds within Allocated Time / Turnarounds
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airport_operations
- **Sector:** airports

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1179 (batch 4)
