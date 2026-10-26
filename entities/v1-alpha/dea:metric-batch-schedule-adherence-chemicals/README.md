# dea:metric-batch-schedule-adherence-chemicals

Candidate Performance Metric record for **Batch Schedule Adherence (Chemicals)** (BSA-C) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-batch-schedule-adherence-chemicals`
- **Name:** Batch Schedule Adherence (Chemicals)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** BSA-C

## 2. Definition

Batch Schedule Adherence (Chemicals) (BSA-C) captures conformance to standards, plans, or obligations for organizations tracking chemicals. It is computed as Batches Produced on Schedule / Batches Planned, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Chemicals.

## Formula

```
Batches Produced on Schedule / Batches Planned
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** chemicals
- **Sector:** chemicals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 897 (batch 3)
