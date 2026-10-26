# dea:metric-vendor-quality-scorecard-average

Candidate Performance Metric record for **Vendor Quality Scorecard Average** (VQSA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-vendor-quality-scorecard-average`
- **Name:** Vendor Quality Scorecard Average
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** VQSA

## 2. Definition

Vendor Quality Scorecard Average (VQSA) captures the quality of outputs and outcomes for organizations tracking outsourcing & vendor management. It is computed as Average Weighted Quality Score across Strategic Vendors, expressed in score (points). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the average composite score across the active vendor pool. It matters because portfolio-level quality trends show whether vendor management is improving or just rotating. Averages hide poor performers behind strong ones. Read with scorecard distribution and Vendor SLA Compliance Rate for the worst quartile to see the true tail risk.

## Formula

```
Average Weighted Quality Score across Strategic Vendors
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** outsourcing_vendor_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1131 (batch 4)
