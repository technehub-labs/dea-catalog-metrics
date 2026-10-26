# dea:metric-measurement-system-analysis-acceptance

Candidate Performance Metric record for **Measurement System Analysis Acceptance** (MSA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-measurement-system-analysis-acceptance`
- **Name:** Measurement System Analysis Acceptance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MSA

## 2. Definition

Measurement System Analysis Acceptance (MSA) addresses the quality of outputs and outcomes and is a fixture of quality management reporting. It is computed as Gage R&R Studies Passing / Studies Conducted, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
MSA = Gage R&R Studies Passing / Studies Conducted
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
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
- **Domain:** quality_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 241 (batch 1)
