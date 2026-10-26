# dea:metric-architecture-review-board-pass-rate

Candidate Performance Metric record for **Architecture Review Board Pass Rate** (ARBPR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-architecture-review-board-pass-rate`
- **Name:** Architecture Review Board Pass Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ARBPR

## 2. Definition

Architecture Review Board Pass Rate (ARBPR) measures the quality of outputs and outcomes in the Software Architecture & Technical Design domain. It is computed as Proposals Approved First Time / Proposals Reviewed, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Proposals Approved First Time / Proposals Reviewed
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** software_architecture_technical_design

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2628 (batch 7)
