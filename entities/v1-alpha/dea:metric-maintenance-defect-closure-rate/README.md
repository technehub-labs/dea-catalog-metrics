# dea:metric-maintenance-defect-closure-rate

Candidate Performance Metric record for **Maintenance Defect Closure Rate** (MDCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-maintenance-defect-closure-rate`
- **Name:** Maintenance Defect Closure Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MDCR

## 2. Definition

Maintenance Defect Closure Rate (MDCR) captures the quality of outputs and outcomes for organizations tracking aviation maintenance repair & overhaul. The formula is Deferred Defects Closed within Limit / Defects - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Airlines & aviation sector.

## Formula

```
Deferred Defects Closed within Limit / Defects
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** aviation_maintenance_repair_overhaul
- **Sector:** airlines_aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1185 (batch 4)
